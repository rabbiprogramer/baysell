from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


def send_email(request, email_subject, to , context ):
    sender_email = settings.EMAIL_SEND_FROM



    email_body = render_to_string('email/email_tenplate.html', context)
    email = EmailMultiAlternatives(
        subject=email_subject,
        body="",
        from_email=sender_email,
        to=to,
    )


    email.attach_alternative(email_body,'text.html', context)


    try:
        email.send()
        return HttpResponse("email sent successfully!")
    except Exception as e:
        return HttpResponse(f'Error sending email:{e}')
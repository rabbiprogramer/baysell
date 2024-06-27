from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as signin, logout as signout
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.
def login(request):
    message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password :
            user = authenticate(request, username=username, password=password)
            if user:
                signin(request, user)

                send_mail(
                    'sucsessfuly login to rabbi vai',
                    f'hey {user.first_name} {user.last_name},\n login complate',
                    settings.EMAIL_SEND_FROM,
                    [user.email],
                    fail_silently = False,
                )
                return redirect('customer:persons')
            else:
                message = "Invalid username or password entered"
        else:
            message = "Username and password is required"
    context = {
        "message":message
    }
    return render(request, 'account/login.html', context)

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if first_name and last_name and email and username and password:
            try:
                # Check if the username already exists
                if User.objects.filter(username=username).exists():
                    raise IntegrityError("Username already exists")
                
                # If the username doesn't exist, create the user
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                return redirect('login')
            except IntegrityError as e:
                return redirect('login')
        else:
            return render(request, 'account/signup.html', {'error': 'All fields are required'})
    return render(request, 'account/signup.html')




def logout (request):

    signout(request)
    return redirect('customer:index')

def mm (request):
    return render(request,'account:mm.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse , Http404
from django.contrib.auth.decorators import login_required
from .models import *


def index(request):

    
    return render(request, 'customer/index.html')


def about(request):
    name = 'rabbi hossain is a good boy'

    context = {
        "name":name
    }
    return render(request,'customer/about.html',context)


@login_required(login_url = "/account/login/")
def persons(request):
    message = None
    all_persons = Person.objects.filter(user = request.user).order_by('name')

    name = request.GET.get('name')
    if name:
        all_persons = all_persons.filter(name__icontains= name)
    
    #create a new person
    delete = request.POST.get('delete')
    delete_all = request.POST.get('delete_all')
    if request.method == 'POST' and delete:
        person = Person.objects.get(id = delete)
        person.delete()
        return redirect ('customer:persons')

    elif request.method == 'POST' and delete_all:
        Person.objects.all().delete()
        return redirect ('customer:persons')

    elif request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        is_married = request.POST.get('is_married')
        bio = request.POST.get('bio')
        height = request.POST.get('height')
        birthday = request.POST.get('birthday')
        birthtime = request.POST.get('birthtime')
        created_at = request.POST.get('created_at')

        if is_married == 'on':
            is_married = True
        else:
            is_married = False
        user = request.user

        if name and age and email and height and birthday:
            Person.objects.create(
                user = user,
                name = name,
                age = age,
                email = email,
                is_married = is_married,
                bio = bio,
                height = height,
                birthday = birthday,
                birthtime = birthtime,
                created_at = created_at,
            )
            return redirect ("customer:persons")
        else:
            message = "taratari sob puron korek na hoi hobe na"

    context = {
        "all_persons":all_persons,
        "message":message,
    }


    return render(request,'customer/persons.html',context)


def update_person(request, id):
    try:
        person = Person.objects.get(id = id)
    except Exception as e:
        raise Http404(f"person dose not exists with id: {id}")
    
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        is_married = request.POST.get('is_married')
        bio = request.POST.get('bio')
        height = request.POST.get('height')

        person.name = name
        person.age = age
        person.email = email
        person.is_married = True if is_married == "on" else False
        person.bio = bio
        person.height = height

        person.save()
        return redirect('customer:persons')

    context= {
        "person":person
    }
    return render(request, 'customer/update_person.html', context)




def shop(request):
    return render(request,'customer/shop.html')
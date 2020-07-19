from django.contrib import messages, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from accounts.models import UserProfile


def register(request):

    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        phone = request.POST['phone']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return render(request,'register.html')
            else:
                user= User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                userprofile=UserProfile(phone=phone,user_id=user.id)
                userprofile.save()
                messages.info(request,'user created successfully')
                messages.info(request,'Please Login')
                return render(request,'login.html')

        else:
            messages.info(request, 'password not matched')
            return render(request, 'register.html')
        return redirect('/')
    else:
        return render(request,'register.html')


def login_view(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                if user.is_staff:
                    return redirect("http://127.0.0.1:8000/dashboard")
                else:
                    return redirect("/")

        else:
            messages.info(request,'Invalid Credentials')
            return render(request,'login.html')
    return render(request,'login.html')


def logout_view(request):
    auth.logout(request)
    return redirect('/')

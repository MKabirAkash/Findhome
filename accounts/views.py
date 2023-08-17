from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if request.method=='POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        uname=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['password2']
        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                messages.error(request,'Usename already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email is already used')
                    return redirect('register')
                else:
                    log_user=User.objects.create_user(username=uname,email=email,first_name=fname,last_name=lname,password=pass1)
                    auth.login(request,log_user)
                    messages.success(request,'You are successfully registered')
                    return redirect('index')
        else:
            messages.error(request,'Passwords doesn\'t match')
            return redirect('register')
    else:
        return render(request,'account/register.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        password=request.POST['password']

        log_user=auth.authenticate(username=uname,password=password)
        if log_user is not None:
            auth.login(request,log_user)
            return redirect('dashboard')
        else:
            messages.error(request,'opps! Check your user name and password again')
            return redirect('login')
    else:
        return render(request,'account/login.html')

def dashboard(request):
    return render(request,'account/dashboard.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return render(request,'pages/index.html')
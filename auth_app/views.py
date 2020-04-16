from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request,'auth_app/index.html',{})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User is sucessfully Logged In')
            return redirect('index')
        else:
            messages.success(request, 'Invalid Credentials! Try again')
            return redirect('login_user')
        
    else:
        return render(request,'auth_app/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, 'You Have been sucessfully logout')
    return redirect('index')   


def register_user(request):
    return render(request,'auth_app/register.html',{})


    
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

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
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already taken!')
                return redirect('register_user')
            else:
                   if User.objects.filter(email=email).exists():
                       messages.error(request,'Email is already been used')
                       return redirect('register_user')
                   else:
                       user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password,username=username)
                       user.save()
                       messages.success(request,"Now you can log in")
                       return redirect('login_user')



        else:
            messages.error(request,'Passwords doesnot matches')
            return redirect('register_user')    







        
        
    else:
        return render(request,'auth_app/register.html',{})
    


    
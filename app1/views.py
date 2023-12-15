from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



@login_required(login_url= 'login/')
def about(requests):
    return render(requests,'about.html')

def contact(requests):
    return render(requests,'contact.html')

def gallery(requests):
    return render(requests,'gallery.html')

@login_required(login_url= 'login/')
def index(requests):
    return render(requests,'index.html')

def services(requests):
    return render(requests,'services.html')



def log_in(requests):
   
    if requests.method == 'POST':
        uname=requests.POST.get('username')
        pass1=requests.POST.get('password')
        user=authenticate(requests,username=uname, password=pass1)
        
        if user is not None:
            login(requests,user)
            return redirect('index')
        else:
            return HttpResponse("Username and Password is incorrect")
        
    return render (requests, 'login.html')
        
    


def sign_up(requests):
    if requests.method == 'POST' :
        uname=requests.POST.get('username')
        email=requests.POST.get('email')
        pass1=requests.POST.get('password1')
        pass2=requests.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Password are not same")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login/')
        
    return render (requests, 'signup.html')


def log_out(requests):
    logout(requests)
    return redirect('login/')
    
          
  

        


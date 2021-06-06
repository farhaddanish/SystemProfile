
from django.contrib.auth import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import signUP, Edit


# Create your views here.






def index(request):
    return render(request, "index.html", {})


def signup_user(request):
    if request.method == 'POST':
        form = signUP(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("SignUP Scussefully"))
            return HttpResponseRedirect("/")

    else:
        form = signUP
        
    context = {"content": form}
    return render(request, "signup.html", context)



def login_user (request):
    if request.method == 'POST':
        email= request.POST["email"]
        password = request.POST["password1"]
        
        form = authenticate(request,username=email ,password=password)
        print(form)
        if form is not None:
            login(request,form)
            messages.success(request, ("Login Scussefully"))
            return HttpResponseRedirect("/")
        else:
            messages.success(request,("try again"))
            return HttpResponseRedirect("/login")

    
    return render(request, "login.html", {}) 


def logout_user (request):
    logout(request)
    messages.success(request,("logout successfully"))
    return HttpResponseRedirect("/")



def edit_user (request):
    if request.method == 'POST':
        form = Edit(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ("edit  Scussefully"))
            return HttpResponseRedirect("/")

    else:
        form = Edit(instance=request.user)
        
    context = {"content": form}
    return render(request, "edit.html", context)




def changePassword (request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request, ("SignUP Scussefully"))
            return HttpResponseRedirect("/")

    else:
        form = PasswordChangeForm(user=request.user)
        
    context = {"content": form}
    return render(request, "change.html", context)

from django.shortcuts import render,redirect

from rest_framework import viewsets
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def registerPage(request):
    
    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created.")
            return redirect('login')
        
    else:
        form = CreateUserForm()
    Context = {"form" : form}
    return render(request,'account/register.html',Context)


def loginPage(request):
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    context ={}
    return render(request,'account/login.html')
    

def resetPage(request):
    context = {}
    return render(request,'account/reset.html',context)

def homePage(request):
    context={}
    return render(request,'account/home.html',context)




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def register(request):
    return render(request, 'register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user) 
            messages.success(request,("You have been logged in successfully!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, please try again!")) 
            return redirect('user_login')
    else:
        return render(request, 'login.html')
    
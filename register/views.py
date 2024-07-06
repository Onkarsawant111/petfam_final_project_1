from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import Register

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            # user login after registration 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have registered and logged in successfully!")
            return redirect('home')
        else:
            # Print form errors to console for debugging
            errors = form.errors
            messages.success(request, errors)
            return redirect('register')
    else:
        form = Register()
        return render(request, 'register.html', {'form': form})

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
            messages.success(request, ("Check the login credentials & Please try again!")) 
            return redirect('user_login')
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')
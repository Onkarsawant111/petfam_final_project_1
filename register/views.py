from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import Register, Userinfo
from products.models import Customer_profile

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
            messages.success(request, "*Please add additional details")
            return redirect('user_info')
        else:
            # Print form errors to console for debugging
            errors = form.errors
            messages.success(request, errors)
            return redirect('register')
    else:
        form = Register()
        return render(request, 'register.html', {'form': form})
    
def user_info(request):  # adding phone no and adress in our User model 
    if request.user.is_authenticated:
        # Attempt to get the Customer_profile for the current user
        try:
            profile = Customer_profile.objects.get(user=request.user)
        except Customer_profile.DoesNotExist:
            profile = None

        if request.method == 'POST':
            form = Userinfo(request.POST, instance=profile)
            if form.is_valid():
                user_info = form.save(commit=False)
                if profile is None:  # Create new profile if it doesn't exist
                    user_info.user = request.user
                user_info.save()
                messages.success(request, "Your info has been updated")
                return redirect('home')
        else:
            form = Userinfo(instance=profile)

        return render(request, 'user_info.html', {'form': form})
    else:
        messages.error(request, "*Error: You must be logged in to access this page.")
        return redirect('register')

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
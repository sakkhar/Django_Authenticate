from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'authenticate/home.html', {})

def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have sucessfully logged in!!'))
            return redirect('home')
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.
            ...
            messages.success(request, ('Error Login-- Please Try Again'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})




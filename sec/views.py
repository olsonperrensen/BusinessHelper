from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def login_user(req):
    if req.method == 'POST':
        user = authenticate(req, username=req.POST['em'], password=req.POST['pwd'])
        if user is not None:
            login(req, user)
            return redirect('homepage')
        else:
            messages.success(req, ("Invalid. Try again"))
            return redirect('login')

    return render(req, 'authenticate/login.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
# Create your views here.


def login_user(req):
    if req.method == 'POST':
        user = authenticate(
            req, username=req.POST['em'], password=req.POST['pwd'])
        if user is not None:
            login(req, user)
            return redirect('homepage')
        else:
            messages.success(req, ("Invalid. Try again"))
            return redirect('login')

    return render(req, 'authenticate/login.html')


def logout_user(req):
    logout(req)
    messages.success(req, ("Logout OK"))
    return redirect('homepage')


def register_user(req):
    if req.method == 'POST':
        form = RegisterUserForm(req.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                req, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(req, user)
            messages.success(req, ("You've registered!"))
    else:
        form = RegisterUserForm()
    return render(req, 'authenticate/register_user.html', {'form': form, })

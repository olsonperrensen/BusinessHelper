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
        # UNKOWN ERROR DURING REGISTRATION WOULD LAND HERE
        else:
            messages.success(req, ("Invalid. Try again"))
            return redirect('login')
    # LINE BELOW NEVER EXECUTES EXCEPT FOR GET REQUEST
    return render(req, 'authenticate/login.html')


def logout_user(req):
    # DESTROY SESSION AND LOGOUT USER
    logout(req)
    # DISPLAY AN ALERT TO THE USER IN THE BASE CLASS TO SAY LOGOUT WENT OK
    messages.success(req, ("Logout OK"))
    return redirect('homepage')


def register_user(req):
    if req.method == 'POST':
        # GRAB POST DATA AND INSTANTIATE OUR CUSTOM OBJECT-FORM-CLASS MADE IN FORMS.PY
        form = RegisterUserForm(req.POST)
        if form.is_valid():
            form.save()
            # NOT ONLY REGISTER BUT LOG IN SIMULTANEOUSLY
            user = authenticate(
                req, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(req, user)
            # LINE BELOW DISPLAYED IN HTML
            messages.success(req, ("You've registered!"))
    else:
        # FIRST TIME VIA GET
        form = RegisterUserForm()
    # INTERPOLATION OF OUR GENERATED FORM WITH THE TEMPLATE SO FIELDS REMAIN IN CASE OF ERRORS (EXCEPT PWD)
    return render(req, 'authenticate/register_user.html', {'form': form, })

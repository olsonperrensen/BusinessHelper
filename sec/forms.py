from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

# CUSTOM FORM THAT USES BOOTSTRAP AND EXTRA ADDED FIELDS
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    manager = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    department = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

# EVERYTHING BELOW WAS BORROWED FROM https://youtu.be/HdrOcreAXKk (credit goes to @Codemycom thus)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'manager', 'department',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

from .models import Profile
from django.db import models
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView


#custom user registration form
class UserRegister(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegister, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'placeholder':'E-mail'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Repeat Password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#custom user login form
class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['password'].widget.attrs.update({'placeholder':'Password'})
    class Meta:
        model = User
        fields = ['username', 'password']


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio', 'contacts']
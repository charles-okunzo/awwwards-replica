from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User

from users.forms import UserRegister


# Create your views here.


class UserRegisterView(CreateView):
    model = User
    template_name = 'users/registration_form.html'
    success_url = '/'
    form_class = UserRegister

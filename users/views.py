from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

from users.forms import CustomLoginForm, UserRegister


# Create your views here.


class UserRegisterView(CreateView):
    model = User
    template_name = 'users/registration_form.html'
    success_url = 'login/'
    form_class = UserRegister


class UserLoginView(LoginView):
    model = User
    template_name = 'users/login.html'
    success_url = '/'
    form_class = CustomLoginForm


def profile(request):
    context = {}
    return render(request, 'users/profile.html', context)



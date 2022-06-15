from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from awwwards_app.models import Project

from users.forms import CustomLoginForm, UpdateProfileForm, UserRegister, UpdateUserForm


# Create your views here.


class UserRegisterView(CreateView):
    model = User
    template_name = 'users/registration_form.html'
    success_url = '/login'
    form_class = UserRegister


class UserLoginView(LoginView):
    model = User
    template_name = 'users/login.html'
    success_url = '/'
    form_class = CustomLoginForm


def profile(request, username):
    my_projects = Project.objects.filter(user__username = username).all()
    context = {
        'projects':my_projects
    }
    return render(request, 'users/profile.html', context)


def update_profile(request, username):
    u_form = UpdateUserForm(instance=request.user)
    p_form = UpdateProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile Updated successfully')
            return redirect('profile', username = username)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile_update.html', context)


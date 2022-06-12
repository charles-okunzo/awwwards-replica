from django.views.generic.list import ListView
from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    title = 'Welcome to awwwards'

    projects = Project.objects.all()
    context = {
        'title': title,
        'projects': projects
    }
    return render(request, 'index.html', context)
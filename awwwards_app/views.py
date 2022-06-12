from django.views.generic import ListView, CreateView
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


class ProjectCreateView(CreateView):
    model = Project
    fields = ['title', 'image', 'link', 'description']
    template_name = 'awwwards_app/create_project.html'
    success_url = '/'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
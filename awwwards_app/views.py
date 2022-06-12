from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import redirect, render

from awwwards_app.forms import RatingForm
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

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'awwwards_app/project-detail.html'
    context_object_name = 'project'


def create_ratings(request, pk):
    form = RatingForm()
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.project = Project.objects.get(pk=pk)
            form.save()
            return redirect('project-detail')
    context = {
        'form':form
    }
    return render(request, 'awwwards_app/rate_project.html', context)
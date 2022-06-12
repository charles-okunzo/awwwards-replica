from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
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

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'awwwards_app/project-detail.html'
    context_object_name = 'project'

class ProjectRateCreateView(CreateView):
    model = Rating
    fields = ['design', 'usability', 'content']
    template_name = 'awwwards_app/rate_project.html'


    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def form_valid(self, form,  pk):
        post = Project.objects.get(pk=pk)
        form.instance.user = self.request.user
        form.instance.project
        return super().form_valid(form)
    


    def get_success_url(self, **kwargs):
        if  kwargs != None:
            post = self.get_object()
            return reverse_lazy('project-detail', kwargs = {'pk': post.id})

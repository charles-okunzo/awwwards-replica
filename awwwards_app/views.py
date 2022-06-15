from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from awwwards_app.forms import RatingForm
from .models import *

# Create your views here.


def home(request):
    title = 'Welcome to awwwards'
    if 'search_proj' in request.GET and request.GET.get('search_proj'):
        search_phrase = request.GET.get('search_proj')
        projects = Project.search_by_title(search_phrase)

        found_proj = projects
        context = {
        'title': title,
        'projects': projects,
        'found_proj':found_proj
        }
        return render(request, 'index.html', context)
    else:
        projects = Project.objects.all().order_by('-date_posted')
        context = {
            'title': title,
            'projects': projects
        }
        return render(request, 'index.html', context)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'image', 'link', 'description']
    template_name = 'awwwards_app/create_project.html'
    success_url = '/'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def show_project_details(request, pk):
    project = Project.objects.get(pk=pk)
    ratings = Rating.objects.filter(project__id = pk)
    total_average = 0
    total_design = 0
    total_usability = 0
    total_content = 0
    for rating in ratings:
        average = rating.ratings_average
        total_average+=average
        total_design+=rating.design
        total_usability+=rating.usability
        total_content+=rating.content
    if len(ratings) > 0:
        grand_average=total_average//len(ratings)#finds the average ratings from all categories by all users
        aver_design = total_design//len(ratings)#calculates average rating for design
        aver_usability = total_usability//len(ratings)#calculates average rating for usability
        aver_content = total_content//len(ratings)# calculates the average rating for content
    else:
        grand_average =0
        aver_design=0
        aver_usability=0
        aver_content=0



    #check vote status i.e. if a user has already voted
    
    ratings = Rating.objects.filter(project = pk).all()
    vote_status = False
    for rating in ratings:
        if rating.user.id == request.user.id:
            vote_status=True
            break
        else:
            vote_status=False
    context = {
        'project':project,
        'ratings':ratings,
        'grand_average':grand_average,
        'aver_design':aver_design,
        'aver_usability':aver_usability,
        'aver_content':aver_content,
        'vote_status':vote_status
    }
    return render(request, 'awwwards_app/project-detail.html', context)



@login_required
def create_ratings(request, pk):
    form = RatingForm()
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.project = Project.objects.get(pk=pk)
            form.save()
            return redirect('project-detail', pk=pk)
    
    context = {
        'form':form,
    }
    return render(request, 'awwwards_app/rate_project.html', context)
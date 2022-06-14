from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/create-new/',views.ProjectCreateView.as_view(), name='create-project'),
    path('project/detail/<int:pk>',views.show_project_details, name='project-detail'),
    path('project/rate/<int:pk>',views.create_ratings, name='rate-project')


]

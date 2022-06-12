from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/create-new/',views.ProjectCreateView.as_view(), name='create-project')
]

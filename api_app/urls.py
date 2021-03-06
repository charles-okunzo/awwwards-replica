from . import views
from django.urls import path


urlpatterns = [
    path('projects-endpoint', views.ProjectAPIView.as_view(), name='project-endpoint'),
    path('profiles-endpoint', views.ProfileAPIView.as_view(), name='profile-endpoint'),
]
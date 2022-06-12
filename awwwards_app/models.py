from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    user = models.ForeignKey(User, related_name='project', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'projects', blank = True, null = True)
    description = models.TextField()
    link = models.CharField(max_length=150)
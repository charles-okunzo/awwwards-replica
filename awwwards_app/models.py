from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    user = models.ForeignKey(User, related_name='project', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'projects', blank = True, null = True)
    description = models.TextField()
    link = models.CharField(max_length=150)


    def __str__(self) -> str:
        return f'{self.title}'


class Rating(models.Model):
    design = models.IntegerField(max_length=10, blank=True)
    usability = models.IntegerField(max_length=10, blank=True)
    content = models.IntegerField(max_length=10, blank=True)
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'{self.user}\'s Ratings'
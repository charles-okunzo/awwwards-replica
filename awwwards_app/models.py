import math
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Project(models.Model):
    user = models.ForeignKey(User, related_name='project', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'projects')
    description = models.TextField()
    link = models.CharField(max_length=150)
    date_posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    @classmethod
    def search_by_title(cls, search_term):
        return cls.objects.filter(title__icontains = search_term).all()


    def __str__(self) -> str:
        return f'{self.title}'


class Rating(models.Model):
    design = models.IntegerField(default=0,validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ] , blank=True)
    usability = models.IntegerField(default=0, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ], blank=True)
    content = models.IntegerField(default=0, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ], blank=True)
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='ratings', on_delete=models.CASCADE)


    @property
    def ratings_average(self):
        return math.ceil((self.design+ self.usability+self.content)/3)
    def __str__(self) -> str:
        return f'{self.user}\'s Ratings'
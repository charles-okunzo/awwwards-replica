from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profile', blank= True)
    bio = models.TextField(blank= True)
    contacts = models.CharField(max_length=100, blank= True)


    def __str__(self) -> str:
        return f'{self.user}\'s Profile'
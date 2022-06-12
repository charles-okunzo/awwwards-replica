from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profile', default = 'user7.jpg', blank= True)
    bio = models.TextField(blank= True)
    contacts = models.CharField(max_length=100, blank= True)


    def save(self, *args, **kwargs):
        super().save(self, *args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.width > 300 or img.height >300:
            output_size = (300, 300)

            img.thumbnail(output_size)
            img.save(self.profile_pic.path)


    def __str__(self) -> str:
        return f'{self.user}\'s Profile'
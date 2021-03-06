from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Scientist(AbstractUser): #user class

    avatar = models.ImageField(upload_to="avatars/")
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)

from django.db import models
from django.db.models import SET_NULL
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.
from accounts.models import Scientist

class Project(models.Model): #user class
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    time_spent = models.CharField(max_length=20)
    likes = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    creator = models.ForeignKey(to=Scientist, related_name='projects',
    null=True, on_delete=SET_NULL)
    url = models.TextField(max_length=200)
    time_added = models.DateTimeField(null=True)

class Comment(models.Model):
    comment = models.TextField(max_length=200)
    author = models.ForeignKey(to=Scientist, related_name='comments',
    null=True, on_delete=SET_NULL)
    project = models.ForeignKey(to=Project, related_name='comments',
    null=True, on_delete=SET_NULL)

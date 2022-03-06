from django.shortcuts import render, redirect
from django.views.generic import FormView, DetailView, ListView, UpdateView

from projects.forms.projectForm import projectForm
from django.utils import timezone
from projects.models import Project
# Create your views here.


class projects(ListView):
    template_name="projects.html"
    queryset = Project.objects.order_by('time_added')[:30] #30 recent projects
    context_object_name = 'projects'

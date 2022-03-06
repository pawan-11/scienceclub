from django.shortcuts import render, redirect
from django.views.generic import FormView, DetailView, ListView, UpdateView

from projects.forms.projectForm import projectForm
from django.utils import timezone
# Create your views here.

class projectFormView(UpdateView):
    template_name = 'projectForm.html'
    model = projectForm
    
    def form_valid(self, form):
        request = self.request
        if not request.user.is_authenticated:
            return redirect("/accounts/login/")

        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        time_spent = request.POST.get('time_spent', '')
        time_added = timezone.now()

        project = Project(name=name, description=description,
        time_spent=time_spent, time_added=time_added, creator=request.user)
        project.save()
        return redirect("/projects/")

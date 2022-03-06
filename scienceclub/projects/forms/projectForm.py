from django import forms
from django.core.exceptions import ValidationError

from projects.models import Project

class projectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'time_spent', 'description', 'url')

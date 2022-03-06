from django.shortcuts import render

from django.views.generic import FormView, DetailView, ListView, UpdateView
from accounts.models import Scientist
# Create your views here.

def index(request):
    return render(request, "index.html")

def faq(request):
    return render(request, "faq.html")

class scientists(ListView):
    template_name="scientists.html"
    queryset = Scientist.objects.all()
    context_object_name = 'scientists'

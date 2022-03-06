from django.shortcuts import render, redirect

from django.views.generic import FormView, DetailView, ListView, UpdateView
from accounts.models import Scientist

# Create your views here.

def index(request):
    return redirect("/community/scientists/")
    #return render(request, "index.html")

class scientists(ListView):
    template_name="scientists.html"
    #queryset = Scientist.objects.all()
    context_object_name = 'scientists'
    queryset = Scientist.objects.order_by('experience')

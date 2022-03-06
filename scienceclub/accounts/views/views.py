from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from accounts.models import Scientist
from django.views.generic import FormView, DetailView, ListView, UpdateView
from projects.models import Project
# Create your views here.


def login(request):
    if request.method == "GET":
        return TemplateResponse(request, "login.html")

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    context = {}
    try:
        user = Scientist.objects.get(username=username)
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
        else:
            context["password_error"] = "Invalid password"
    except:
        context["username_error"] = "Username is not registered"

    if len(context) > 0:
        return render(request, "login.html", context)

    return redirect("/accounts/profile/view/")

def signup(request):
    if request.method=="GET":
        return render(request, "signup.html")
    username = request.POST.get('username', '')
    password1 = request.POST.get('password1', '')
    password2 = request.POST.get('password2', '')
    email = request.POST.get('email', '')
    context = {}
    if password1 != password2:
        context['error'] = "Passwords do not match"
    if not username:
        context['error'] = "Enter a username"
    if not password1:
        context['error'] = "Enter a password"
    try:
        existing_user = User.objects.get(username=username)
        context['error'] = "Username exists"
    except:
        pass
    if email:
        try:
            validate_email(email)
        except:
            context['error'] = "Email is invalid"
    if context.get('error'):
        return render(request=request, template_name="signup.html", context=context)

    Scientist.objects.create_user(username=username, password=password1,
    email=email)

    return redirect("/accounts/login/")

def viewProfile(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("/accounts/login/")
    context = {}
    context['projects'] = user.projects.all()
    #context['projects'] = Project.objects.filter(creator=user)
    return render(request, "viewProfile.html", context=context)

def editProfile(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login/")

    if request.method=="GET":
        return render(request, "editProfile.html")

    email = request.POST.get('email', '')
    password1 = request.POST.get('password1', '')
    password2 = request.POST.get('password2', '')
    context = {}
    if password1:
        if password1 != password2:
            context['error'] = "Passwords do not match"
    if email:
        try:
            validate_email(email)
        except:
            context['error'] = "Email is invalid"
    if len(context) > 0:
        return render(request, "editProfile.html", context=context)
    return redirect("/accounts/profile/view/")

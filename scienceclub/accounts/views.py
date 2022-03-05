from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def viewProfile(request):
    return render(request, "viewProfile.html")

def editProfile(request):
    return render(request, "editProfile.html")

def topProfiles(request):
    return render(request, "topProfiles.html")

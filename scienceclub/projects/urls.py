from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from projects.views.views import projects
from projects.views.projectFormView import projectFormView

app_name='projects'

urlpatterns = [
    path('', projects.as_view(), name='projects'),
    path('add/', projectFormView.as_view(), name='addProject'),
]

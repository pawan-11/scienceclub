from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from community.views.views import index, scientists

app_name='community'

urlpatterns = [
    path('', index, name='index'),
    path('scientists/', scientists.as_view(), name='scientists'),
]

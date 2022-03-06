from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.views.views import signup, login, viewProfile, editProfile

app_name='accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('viewProfile/', viewProfile, name='viewProfile'),
    path('editProfile/', editProfile, name='signup'),
]

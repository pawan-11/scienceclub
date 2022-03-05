from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from community.views import index

app_name='accounts'

urlpatterns = [
    path('', index, name='index'),

]

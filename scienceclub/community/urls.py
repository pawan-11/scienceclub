from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from community.views.views import index, faq, scientists

app_name='accounts'

urlpatterns = [
    path('', index, name='index'),
    path('faq/', faq, name='faq'),
    path('scientists/', scientists.as_view(), name='scientists'),
]

from django.urls import path
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken 

urlpatterns = [
    path('register/',Register.as_view()),
    path('login/',ObtainAuthToken.as_view()),
]
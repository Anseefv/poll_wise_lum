from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView,mixins

from .models import*
from .serializers import*


class Register(CreateAPIView):

    serializer_class=CustomUserSerializer
    
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from home.models import Settings
from .serializers import UserSerializer, UserSettingsSerializers

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSettingsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Settings.objects.all()
    serializer_class = UserSettingsSerializers
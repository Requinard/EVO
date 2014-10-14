from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from home.models import Settings, Location
from .serializers import UserSerializer, UserSettingsSerializers, UserLocationSerializers

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

class UserLocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = UserLocationSerializers
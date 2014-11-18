from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from users.models import UserSettings, UserLocation
from .serializers import UserSerializer, UserSettingsSerializers, UserLocationSerializers

# Create your views here.
def exception_handler(exc):
    print exc

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
    queryset = UserSettings.objects.all()
    serializer_class = UserSettingsSerializers

class UserLocationViewSet(viewsets.ModelViewSet):
    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSerializers
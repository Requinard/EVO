from django.contrib.auth.models import User, Group
from users.models import UserSettings, UserLocation
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'groups')

class UserSettingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserSettings

class UserLocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserLocation

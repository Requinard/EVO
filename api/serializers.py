from django.contrib.auth.models import User, Group
from home.models import Settings
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'groups')

class UserSettingsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Settings
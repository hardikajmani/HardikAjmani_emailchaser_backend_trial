from rest_framework import serializers
from .models import User, ConnectedEmail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email")


class ConnectedEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectedEmail
        fields = ("id", "user", "email", "password", "provider")

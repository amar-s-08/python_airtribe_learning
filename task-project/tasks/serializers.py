from rest_framework import serializers
from .models import User

# Manual Serialization
# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=100)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
from rest_framework import serializers
from .models import Task, User

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

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "user", "title", "description", "completed", "created_at", "updated_at", "due_date"]
        read_only_fields = ["id", "created_at", "updated_at"]
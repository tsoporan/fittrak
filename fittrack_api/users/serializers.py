from rest_framework import serializers
from .models import User, Profile

class ProfileSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    date_created = serializers.DateTimeField()

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile', 'is_active')

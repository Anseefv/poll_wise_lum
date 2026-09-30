from rest_framework import serializers
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','password','email']
        read_only_fields=['id']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
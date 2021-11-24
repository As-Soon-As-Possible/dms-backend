from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Victim


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]



class VictimSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        victim = Victim.objects.create_user(**validated_data)
        return victim

    class Meta:
        model = User
        fields = (
            'name',
            'mobile_no',
            'location',
            'latitude',
            'longitude',
            'additional_info',
        )

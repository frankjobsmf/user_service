#rest_framework
from rest_framework import serializers

#django user model
from django.contrib.auth.models import User

#user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email'
        )
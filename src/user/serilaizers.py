from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework.response import Response 


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
     
class UserReadSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ('id', 'date_joined')
        
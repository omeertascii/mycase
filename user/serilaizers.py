from rest_framework import serializers, status
from .serilaizers import UserCreateSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response 


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        
        def post(self, request, *args, **kwargs):
            serializer = UserCreateSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserReadSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ('id', 'date_joined')
        
from rest_framework import serializers
from django.contrib.auth.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
     
class UserReadSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ('id', 'date_joined')
        
        
class LoginSerilaizer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = User.objects.filter(username=username).first()
            if user is None:
                raise serializers.ValidationError("User not found")
            if not user.check_password(password):
                raise serializers.ValidationError("Password is wrong")
            return user
        else:
            raise serializers.ValidationError("Username and password must be filled")
        
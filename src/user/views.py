from .serilaizers import UserCreateSerializer, LoginSerilaizer
from .models import User
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    
    def get_serilaizer_class(self):
        if self.action == 'login':
            return LoginSerilaizer
        return UserCreateSerializer
    
    @action(detail=False, methods=["POST"], url_path="login", url_name="login")
    
    def login(self, request):
        serilaizer = LoginSerilaizer(data=request.data)
        
        if serilaizer.is_valid():
            token = serilaizer.save()
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        
        elif serilaizer.errors:
            return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

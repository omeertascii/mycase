from .serilaizers import UserCreateSerializer, LoginSerilaizer
from .models import User
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    
    # TODO: get serializer class fonksiyonu yaz login için özelleştir.

    # TODO: login view yazılacak
    # @action
    # model User
    # login seriliazer yazılacak
    # serializer fields username - passsword
    # hata varsa hata dönülecek şifre yanlışsa filan
    # response serializer yazılacak token dönecek
    # restframework token
    
    @action(detail=False, methods=["POST"], url_path="login", url_name="login")
    
    def login(self, request):
        serilaizer = LoginSerilaizer(data=request.data)
        
        if serilaizer.is_valid():
            token = serilaizer.save()
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        
        elif serilaizer.errors:
            return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

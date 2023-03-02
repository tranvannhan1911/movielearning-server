from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import status, generics, viewsets
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from core_movie.serializers.user import UserSerializers
from ..utils.perms import *
from ..utils.apicodes import ApiCode
from django.contrib.auth.models import User

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView ): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializers
    
    # @method_permission_classes((IsAuthenticated,))
    # @action(methods = ['GET'], detail = True) 
    # def get(seft, request): 
    #     u = User.objects.all()
    #     return Response(data=UserSerializers(u, context = {'request': request}, many=True).data, status = status.HTTP_200_OK)

        
            
    
    
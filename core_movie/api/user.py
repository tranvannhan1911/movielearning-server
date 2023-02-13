from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import status, generics, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from core_movie.serializers.user import UserSerializers


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView ): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializers
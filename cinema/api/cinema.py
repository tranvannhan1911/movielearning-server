from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

from drf_yasg.utils import swagger_auto_schema
from core_movie import swagger
from core_movie.swagger import SwaggerSchema

from django.views.decorators.csrf import csrf_exempt
from core_movie.serializers.movie import MovieSerializer,SubsSerializer
from core_movie.utils.apicodes import ApiCode
from core_movie.models import Movie,Subs
from cinema.models import Showtime
from cinema.serializers.cinema import CinemaShowtimeSerializer
from bson.objectid import ObjectId
# 
class CinemaRoomView(generics.ListAPIView):
    # permission_classes = [AllowAny, ]
    # serializer_class = MovieSerializer

    # @swagger_auto_schema(
    #     manual_parameters=[SwaggerSchema.token],
    #     query_serializer=MovieSerializer,
    #     responses={200: swagger.movie_info["list"]})
    def get(self, request, *args, **kwargs):
        serializer = CinemaShowtimeSerializer(Showtime.objects.first())
        return Response(data=ApiCode.success(data=serializer.data),
            status=status.HTTP_200_OK)


class CinemaShowtimeView(generics.ListAPIView):
    # permission_classes = [AllowAny, ]
    # serializer_class = MovieSerializer

    # @swagger_auto_schema(
    #     manual_parameters=[SwaggerSchema.token],
    #     query_serializer=MovieSerializer,
    #     responses={200: swagger.movie_info["list"]})
    def get(self, request, showtime_id):
        if Showtime.objects.filter(pk=ObjectId(showtime_id)).count() == 0:
            return Response(
                data=ApiCode.error(message="Không tồn tại"),
                status=status.HTTP_200_OK)
                
        showtime = Showtime.objects.get(pk=ObjectId(showtime_id))
        serializer = CinemaShowtimeSerializer(showtime)
        return Response(data=ApiCode.success(data=serializer.data),
            status=status.HTTP_200_OK)
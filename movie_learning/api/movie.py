from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework import status

from movie_learning.serializers.movie import MovieSerializer,WatchMovieSerializer
from movie_learning.utils.apicodes import ApiCode
from movie_learning.models import Movie
from movie_learning import swagger
from movie_learning.swagger import SwaggerSchema

class MovieView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'head']
    @swagger_auto_schema(
        manual_parameters=[SwaggerSchema.token],
        request_body=MovieSerializer,
        responses={200: swagger.movies["get"]})
    def get(self, request, format=None):
        serializer =MovieSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)

    def post(self, request, format=None):
        self.http_method_names.append("GET")

        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            movie = serializer.save()
            response = WatchMovieSerializer(movie)
            return Response(data = ApiCode.success(data=response.data), status = status.HTTP_200_OK)
        return Response(data = ApiCode.error(message=serializer.errors), status = status.HTTP_200_OK)


    def get_queryset(self):
        return Movie.objects.all().order_by("-release_date")

    @swagger_auto_schema(
        manual_parameters=[SwaggerSchema.token],
        responses={200: swagger.movies["list"]})
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        active = request.query_params.get('active')
        if active:
            queryset = queryset.filter(status=True)
            queryset = [x for x in queryset]

        response = WatchMovieSerializer(data=queryset, many=True)
        response.is_valid()
        return Response(data = ApiCode.success(data={
            "count": len(response.data),
            "results": response.data
        }), status = status.HTTP_200_OK)

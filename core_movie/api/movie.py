from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema
from core_movie import swagger
from core_movie.swagger import SwaggerSchema

from django.views.decorators.csrf import csrf_exempt
from core_movie.serializers.movie import MovieSerializer,SubsSerializer
from core_movie.utils.apicodes import ApiCode
from core_movie.models import Movie,Subs

@swagger_auto_schema(method='GET',
        manual_parameters=[SwaggerSchema.token],
        query_serializer=MovieSerializer,
        responses={200: swagger.movie_info["list"]})
@swagger_auto_schema(method='POST',
        manual_parameters=[SwaggerSchema.token],
        request_body=MovieSerializer,
        responses={200: swagger.movie_info["get"]})
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def all_movie(request,id=0):
    if request.method=='GET':
        movies = Movie.objects.all()
        movies_serializer=MovieSerializer(movies,many=True)
        return Response(data=ApiCode.success(data=movies_serializer.data,message="getAllMovie"),status=status.HTTP_200_OK)
    elif request.method=='POST':
        movie_data=JSONParser().parse(request)
        movies_serializer=MovieSerializer(data=movie_data)
        if movies_serializer.is_valid():
            movies_serializer.save()
            return Response("Added Successfully",status=status.HTTP_201_CREATED)
        return Response("Failed to Add", status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        movie_data=JSONParser().parse(request)
        movie=Movie.objects.get(id=movie_data['movie_id'])
        movies_serializer=MovieSerializer(movie,data=movie_data)
        if movies_serializer.is_valid():
            movies_serializer.save()
            return Response("Updated Successfully")
        return Response("Failed to Update")

@swagger_auto_schema(method='GET',
        manual_parameters=[SwaggerSchema.token],
        query_serializer=MovieSerializer,
        responses={200: swagger.movie_info["get"]})
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def movie_detail(request, movie_id):
    if request.method=='GET':
        movie = Movie.objects.get(movie_id=movie_id)
        movie_serializer=MovieSerializer(movie)
        return Response(data=ApiCode.success(data=movie_serializer.data,message="getMovieDetail"),status=status.HTTP_200_OK)
    elif request.method=='POST':
        movie_data=JSONParser().parse(request)
        movies_serializer=MovieSerializer(data=movie_data)
        if movies_serializer.is_valid():
            movies_serializer.save()
            return Response("Added Successfully",status=status.HTTP_201_CREATED)
        return Response("Failed to Add", status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        movie_data=JSONParser().parse(request)
        movie=Movie.objects.get(id=movie_data['movie_id'])
        movies_serializer=MovieSerializer(movie,data=movie_data)
        if movies_serializer.is_valid():
            movies_serializer.save()
            return Response("Updated Successfully")
        return Response("Failed to Update")
    elif request.method=='DELETE':
        movie=Movie.objects.get(movie_id=movie_id)
        movie.delete()
        return Response("Deleted Successfully")

    def get_queryset(self):
        return Movie.objects.all().order_by("-level")

# GET_SUBS
@swagger_auto_schema(method='GET',

        manual_parameters=[SwaggerSchema.token],
        query_serializer=SubsSerializer,
        responses={200: swagger.movie_sub["get"]})
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def movie_subs(request,movie_id):
    if request.method=='GET':
        subs = Subs.objects.filter(movie_id=movie_id)
        subs_serializer=SubsSerializer(subs,many=True)
        return Response(data=ApiCode.success(data=subs_serializer.data,message="getMovieSubs"),status=status.HTTP_200_OK)
    elif request.method=='POST':
        subs_data=JSONParser().parse(request)
        subs_serializer=SubsSerializer(data=subs_data)
        if subs_serializer.is_valid():
            subs_serializer.save()
            return Response("Added Successfully",status=status.HTTP_201_CREATED)
        return Response("Failed to Add", status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        subs_data=JSONParser().parse(request)
        sub=Subs.objects.get(movie_id=subs_data['movie_id'])
        subs_serializer=SubsSerializer(sub,data=subs_data)
        if subs_serializer.is_valid():
            subs_serializer.save()
            return Response("Updated Successfully")
        return Response("Failed to Update")
    elif request.method=='DELETE':
        sub=Subs.objects.get(movie_id=movie_id)
        sub.delete()
        return Response("Deleted Successfully")
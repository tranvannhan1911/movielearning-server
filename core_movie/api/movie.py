from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from core_movie.serializers.movie import MovieSerializer
from core_movie.utils.apicodes import ApiCode
from core_movie.models import Movie

@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def all_movie(request,id=0):
    if request.method=='GET':
        movies = Movie.objects.all()
        movies_serializer=MovieSerializer(movies,many=True)
        return Response(data=ApiCode.success(data=movies_serializer.data),status=status.HTTP_200_OK)
    elif request.method=='POST':
        movie_data=JSONParser().parse(request)
        movies_serializer=MovieSerializer(data=movie_data)
        if movies_serializer.is_valid():
            movies_serializer.save()
            return Response("Added Successfully",status=status.HTTP_201_CREATED)
        return Response("Failed to Add", status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        movie_data=JSONParser().parse(request)
        movie=Movie.objects.get(movie_id=movie_data['movie_id'])
        movies_serializer=MovieSerializer(movie,data=movie_data)
        if movies_serializer.is_valid():
            movies_serializer.save()
            return Response("Updated Successfully")
        return Response("Failed to Update")
    elif request.method=='DELETE':
        movie=Movie.objects.get(movie_id=id)
        movie.delete()
        return Response("Deleted Successfully")

@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def movie_detail(request, movie_id):
    if request.method=='GET':
        movie = Movie.objects.get(movie_id=movie_id)
        movie_serializer=MovieSerializer(movie)
        return Response(data=ApiCode.success(data=movie_serializer.data),status=status.HTTP_200_OK)
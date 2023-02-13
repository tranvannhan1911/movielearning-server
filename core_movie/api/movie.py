from rest_framework.response import Response 
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny

from drf_yasg.utils import swagger_auto_schema
from core_movie import swagger
from core_movie.swagger import SwaggerSchema

from django.views.decorators.csrf import csrf_exempt
from core_movie.serializers.movie import MovieSerializer,SubsSerializer
from core_movie.utils.apicodes import ApiCode
from core_movie.models import Movie,Subs
from django.contrib.auth.models import User

#List Movie
class AllMovieView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny, ]
    serializer_class = MovieSerializer
    def get_queryset(self):
        return Movie.objects.all()

    @swagger_auto_schema(
        manual_parameters=[SwaggerSchema.token],
        query_serializer=MovieSerializer,
        responses={200: swagger.movie_info["list"]})
    def get(self, request, *args, **kwargs):
        # All Movies
        movies = self.get_queryset()
        total = Movie.objects.count()

        # Pagination
        page = request.GET.get('page', 1)
        if page:
            page = int(page)
        per_page = 24
        start = (page -1) * per_page
        end = page * per_page

        # Serializer
        serializer = MovieSerializer(data=movies[start:end], many= True)
        serializer.is_valid()
        return Response(data=ApiCode.success(
            message="getAllMovie",
            count=len(serializer.data),
            total=total,
            data=serializer.data,
            ),
            status=status.HTTP_200_OK)


# Movie Detail
class MovieIdView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny, ]
    serializer_class = MovieSerializer

    def get_queryset(self, movie_id):
        return Movie.objects.get(movie_id=movie_id)

    @swagger_auto_schema(
        manual_parameters=[SwaggerSchema.token],
        responses={200: swagger.movie_info["get"]})
    def get(self, request, movie_id):
        movie = Movie.objects.get(movie_id=movie_id)
        movie_serializer=MovieSerializer(movie)
        return Response(data=ApiCode.success(data=movie_serializer.data,message="getMovieDetail"),status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[SwaggerSchema.token],
        request_body=MovieSerializer,
        responses={200: swagger.movie_info["get"]})
    def put(self, request, movie_id):
        if not Movie.objects.filter(movie_id = movie_id).exists():
            return Response(data=ApiCode.error(message="Phim không tồn tại"),status=status.HTTP_200_OK)
        movie = Movie.objects.get(movie_id = movie_id)
        serializer = MovieSerializer(movie,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data = ApiCode.success(data=serializer.data), status = status.HTTP_200_OK)
        return Response(data = ApiCode.error(message=serializer.errors), status = status.HTTP_200_OK)


# # GET_SUBS
class SubsView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny, ]
    serializer_class = SubsSerializer

    @swagger_auto_schema(
            manual_parameters=[SwaggerSchema.token],
            query_serializer=SubsSerializer,
            responses={200: swagger.movie_sub["get"]})

    def get(self, request, movie_id):
        subs = Subs.objects.filter(movie_id=movie_id)
        subs_serializer=SubsSerializer(subs,many=True)
        return Response(data=ApiCode.success(data=subs_serializer.data,message="getMovieSubs"),status=status.HTTP_200_OK)



#     elif request.method=='POST':
#         subs_data=JSONParser().parse(request)
#         subs_serializer=SubsSerializer(data=subs_data)
#         if subs_serializer.is_valid():
#             subs_serializer.save()
#             return Response("Added Successfully",status=status.HTTP_201_CREATED)
#         return Response("Failed to Add", status=status.HTTP_400_BAD_REQUEST)


    
    
     
    


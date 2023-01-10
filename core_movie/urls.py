from django.contrib import admin
from django.urls import path,include
from core_movie.api import movie


urlpatterns = [
    path('',movie.all_movie,name='all_movie_api'),
    path('<str:movie_id>/',movie.movie_detail,name='movie_detail_api'),
    path('<str:movie_id>/subtitle/',movie.movie_subs,name='movie_subs_api'),
]

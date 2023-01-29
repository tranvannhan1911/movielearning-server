from django.contrib import admin
from django.urls import path,include
from core_movie.api.movie import AllMovieView,MovieIdView,SubsView


urlpatterns = [
    path('',AllMovieView.as_view(),name='all_movie_api'),
    path('<str:movie_id>/',MovieIdView.as_view(),name='movie_detail_api'),
    path('<str:movie_id>/subtitle/',SubsView.as_view(),name='movie_subs_api'),
]


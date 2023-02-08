from django.contrib import admin
from django.urls import path,include
from core_movie.api.movie import AllMovieView,MovieIdView,SubsView, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter() 
router.register('user', UserViewSet) 
urlpatterns = [
    path('',AllMovieView.as_view(),name='all_movie_api'),
    path('User/', include(router.urls)),
    path('<str:movie_id>/',MovieIdView.as_view(),name='movie_detail_api'),
    path('<str:movie_id>/subtitle/',SubsView.as_view(),name='movie_subs_api'),   
]


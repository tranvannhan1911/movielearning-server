from django.urls import path

from . import views
from .api.cinema import CinemaRoomView, CinemaShowtimeView

urlpatterns = [
    # path("", views.index, name="index"),
    # path("<str:room_name>/", views.room, name="room"),
    path("room/<str:room_name>/", CinemaRoomView.as_view()),
    path("showtime/<str:showtime_id>/", CinemaShowtimeView.as_view()),
]
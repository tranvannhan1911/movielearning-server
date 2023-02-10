from rest_framework import serializers
from cinema.models import Showtime

class CinemaShowtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Showtime
        fields='__all__'
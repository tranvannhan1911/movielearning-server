from django.contrib import admin
from .models import Showtime
# Register your models here.

class ShowtimeAdmin(admin.ModelAdmin):
    fields = [field.name for field in Showtime._meta.get_fields()]
    list_display = [field.name for field in Showtime._meta.get_fields()]
    search_fields = [field.name for field in Showtime._meta.get_fields()]

# admin.site.register(CinemaRoom)
admin.site.register(Showtime)
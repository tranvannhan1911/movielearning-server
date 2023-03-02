# Register your models here.
from django.contrib import admin
from core_movie.models import Movie, ProfileUser, MovieGroup

class MovieGroupInlineAdmin(admin.TabularInline): 
    model = MovieGroup.movies.through
    
class MovieGroupAdmin(admin.ModelAdmin):
    class Media: 
        inlines = (MovieGroupInlineAdmin,)


admin.site.register(Movie)
admin.site.register(ProfileUser)
admin.site.register(MovieGroup, MovieGroupAdmin)
# admin.site.register(Subs)

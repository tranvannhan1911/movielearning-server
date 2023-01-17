
from core_movie.models import Movie, Subs
from bson.objectid import ObjectId

def run():
    movies = Movie.objects.all()
    for movie in movies:
        movie.delete()
        # print(movie.genres)
        # for genres in movie.genres:
        #     genres.movie.genres = ObjectId()
        #     genres.movie.save()
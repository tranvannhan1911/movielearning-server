from crawl import crawl
from core_movie.models import Movie, Subs
from bson.objectid import ObjectId

def run():
    movie_ids = Movie.objects.all().values("movie_id")
    cnt = len(movie_ids)
    idx = 1
    for movie_id in movie_ids:
        movie_id = movie_id["movie_id"]
        print(idx, cnt, movie_id)
        idx+=1
        if Subs.objects.filter(movie_id = movie_id).exists():
            print("skipped")
            continue
        sub = crawl.getSubs(movie_id)
        sub["movie_id"] = movie_id
        sub.pop("_id")
        for i in range(len(sub["sub"])):
            sub["sub"][i]["id"] = ObjectId()
        Subs.objects.create(**sub)
        print("ok")
        # print(subs)


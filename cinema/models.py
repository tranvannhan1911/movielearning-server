from djongo import models
from bson.objectid import ObjectId

# Create your models here.

# class CinemaRoom(models.Model):
#     # id = models.ObjectIdField(default=ObjectId)
#     name = models.TextField()
#     row_count = models.IntegerField()
#     column_count = models.IntegerField()

#     def __str__(self):
#         return self.name

class Showtime(models.Model):
    _id = models.ObjectIdField()
    # id = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    name = models.TextField()
    link_video = models.TextField()

    objects = models.DjongoManager()
    # cinemaroom = models.ForeignKey(CinemaRoom, related_name='showtimes', on_delete=models.PROTECT)
    # movie = models.ForeignKey('core_movie.Movie', related_name='showtimes', on_delete=models.PROTECT)

    # def __str__(self):
    #     return self.name
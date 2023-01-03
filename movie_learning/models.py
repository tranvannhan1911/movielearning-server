from uuid import uuid4
import datetime

from django.db import models
from django.db.models.aggregates import Sum
from django.conf import settings

def created_updated(obj, request):
    obj.save()

class HierarchyTree(models.Model):
    code = models.CharField('Mã code', max_length=30, unique=True)
    name = models.CharField('Tên cấp', max_length=50)
    level = models.IntegerField('Cấp', default=0)
    type = models.CharField('Loại', max_length=15, choices=(
        ("movie", "Phim"),
    ))
    parent = models.ForeignKey("movie_learning.HierarchyTree",
        on_delete=models.CASCADE, null=True, related_name='children')
    note = models.TextField('Ghi chú', null=True)

    class Meta:
        db_table = 'HierarchyTree'


    def get_all_children_id(self):
        ret = []
        queue = []
        queue.append(self)
        while(len(queue) > 0):
            cur = queue.pop(0)
            ret.append(cur.id)
            for child in cur.children.all():
                queue.append(child)
        return ret


class MovieManager(models.Manager):
    def all_with_related_categorys(self):
        qs = self.get_queryset()
        qs = qs.select_related('category')
        qs = qs.prefetch_related('writers', 'actors')
        return qs

    def all_with_related_persons_and_score(self):
        qs = self.all_with_related_categorys()
        qs = qs.annotate(score=Sum('vote__value'))
        return qs

    def top_movies(self, limit=10):
        qs = self.get_queryset()
        qs = qs.annotate(vote_sum=Sum('vote__value'))
        qs = qs.exclude(vote_sum=None)
        qs = qs.order_by('-vote_sum')
        qs = qs[:limit]
        return qs

class Translate(models.Model):
    lang = models.CharField(max_length=7)
    title = models.TextField()
    overview: models.TextField()

class Movie(models.Model):
    RATED_LEVEL_ONE = 1
    RATED_LEVEL_TWO = 2
    RATED_LEVEL_THREE = 3
    RATED_LEVEL_FOUR = 4
    RATINGS = (
        (RATED_LEVEL_ONE, 'FRESHER'),
        (RATED_LEVEL_TWO, 'JUNIOR'),
        (RATED_LEVEL_THREE, 'SENIOR'),
        (RATED_LEVEL_FOUR, 'MASTER'),
    )
    title = models.CharField(max_length=255)
    type = models.TextField()
    poster_path = models.TextField()
    original_language = models.TextField()
    release_date = models.DateField()
    active = models.BooleanField(default=True)
    overview = models.TextField()
    level = models.IntegerField(choices=RATINGS, default=RATED_LEVEL_ONE)
    runtime = models.PositiveIntegerField()
    number_of_seasons = models.PositiveIntegerField()
    number_of_episodes = models.PositiveIntegerField()
    localizes = models.ManyToManyField(Translate)
    product_category = models.ForeignKey(HierarchyTree, on_delete=models.PROTECT,
        related_name='movies', null=True)
    objects = MovieManager()

    class Meta:
        db_table = 'Movie'

    def __str__(self):
        return '{} ({})'.format(self.title, self.release_date)


class VoteManager(models.Manager):
    def get_vote_or_unsaved_blank_vote(self, movie, user):
        try:
            return Vote.objects.get(movie=movie, user=user)
        except Vote.DoesNotExist:
            return Vote(movie=movie, user=user)


class Vote(models.Model):
    UP = 1
    DOWN = -1
    VALUE_CHOICES = (
        (UP, "👍"),
        (DOWN, "👎")
    )

    value = models.SmallIntegerField(choices=VALUE_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    voted_on = models.DateTimeField(auto_now=True)

    objects = VoteManager()

    class Meta:
        unique_together = ('user', 'movie')


def movie_directory_path_with_uuid(instance, filename):
    return '{}/{}'.format(instance.movie_id, uuid4())


class MovieImage(models.Model):
    image = models.ImageField(upload_to=movie_directory_path_with_uuid)
    uploaded = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

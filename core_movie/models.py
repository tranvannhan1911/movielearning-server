from djongo import models  as djongoModels
from django import forms
from django.utils import timezone
from bson.objectid import ObjectId
from django.contrib.auth.models import User
# from django.db import models 

# Create your models here.

class Translate(djongoModels.Model):
    id = djongoModels.ObjectIdField(default=ObjectId, primary_key=True)
    cueStart = djongoModels.IntegerField()
    transcript = djongoModels.TextField()
    cueEnd = djongoModels.IntegerField()
    transcript_vi = djongoModels.TextField()
    seq = djongoModels.IntegerField(default=0)

    def __str__(self):
        return '%s %s' % (self.cueStart, self.cueEnd)

class TranslateForm(forms.ModelForm):
    class Meta:
        model = Translate
        fields = ('cueStart','transcript','cueEnd','transcript_vi','seq')

class Localize(djongoModels.Model):
    id = djongoModels.ObjectIdField(primary_key=True)
    lang = djongoModels.CharField(max_length=5,default="abc")
    title = djongoModels.TextField(default="abc")
    overview = djongoModels.TextField(default="abc")

    def __str__(self):
        return '(%s) %s' % (self.lang, self.title)

class LocalizeForm(forms.ModelForm):
    class Meta:
        model = Localize
        fields = ('lang','title','overview')

class Genres(djongoModels.Model):
    mongo_id = djongoModels.ObjectIdField()
    id = djongoModels.IntegerField(default=0)
    display_name = djongoModels.CharField(max_length=255,default="abc")
    name = djongoModels.CharField(max_length=255,default="abc")

    def __str__(self):
        return '(%s) %s' % (self.id, self.display_name)

class GenresForm(forms.ModelForm):
    class Meta:
        model = Genres
        fields = ('id','display_name','name')

class Subs(djongoModels.Model):
    sub = djongoModels.ArrayField(
            model_container=Translate,
            model_form_class=TranslateForm
        )
    movie_id = djongoModels.CharField(primary_key=True, max_length=255,default=" ")

    objects = djongoModels.DjongoManager()


class Movie(djongoModels.Model):
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
    title = djongoModels.CharField(max_length=255,default="abc")
    apiId = djongoModels.IntegerField(default=0)
    type = djongoModels.TextField(default="abc")
    poster_path = djongoModels.TextField(default="abc")
    backdrop_path = djongoModels.TextField(default="abc")
    release_date = djongoModels.DateField(default=timezone.now)
    trailer_key = djongoModels.CharField(max_length=255,default="abc")
    overview = djongoModels.TextField(default="abc")
    localizes = djongoModels.ArrayField(
        model_container=Localize,
        model_form_class=LocalizeForm
    )
    genres = djongoModels.ArrayField(
        model_container=Genres,
        model_form_class=GenresForm
    )
    level = djongoModels.IntegerField(choices=RATINGS, default=RATED_LEVEL_ONE)
    number_of_seasons = djongoModels.IntegerField(default=0)
    number_of_episodes = djongoModels.IntegerField(default=0)
    video_url = djongoModels.TextField(default="abc")
    link_mp4 = djongoModels.TextField(default=None)
    dateFirstPublished = djongoModels.DateTimeField(default=timezone.now)
    movie_id = djongoModels.CharField(primary_key=True, max_length=255,default=" ")

    objects = djongoModels.DjongoManager()

# class User(djongoModels.Model):
#     user_id = djongoModels.AutoField(primary_key=True)
#     name = djongoModels.CharField(max_length=500)
#     age = djongoModels.IntegerField()

class ProfileUser(djongoModels.Model): 
    user = djongoModels.OneToOneField(
        User, 
        on_delete = djongoModels.CASCADE, 
        null = True
    )
    zalo = djongoModels.CharField(max_length=50)
    

from rest_framework import serializers
from ..models import Movie,Subs, MovieGroup

# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Movie
#         fields='__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=['movie_id','title','apiId','type','poster_path','backdrop_path',
        'release_date','trailer_key','overview','localizes','genres','level',
        'number_of_seasons','number_of_episodes','video_url','dateFirstPublished']

    def get_codes(self, obj):
        return_data = None
        if type(obj.codes) == list:
            embedded_list = []
            for item in obj.codes:
                embedded_dict = item.__dict__
                for key in list(embedded_dict.keys()):
                    if key.startswith('_'):
                        embedded_dict.pop(key)
                embedded_list.append(embedded_dict)
            return_data = embedded_list
        else:
            embedded_dict = obj.embedded_field
            for key in list(embedded_dict.keys()):
                if key.startswith('_'):
                    embedded_dict.pop(key)
            return_data = embedded_dict
        return return_data

class SubsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subs
        fields=['movie_id','sub']
    def get_codes(self, obj):
        return_data = None
        if type(obj.codes) == list:
            embedded_list = []
            for item in obj.codes:
                embedded_dict = item.__dict__
                for key in list(embedded_dict.keys()):
                    if key.startswith('_'):
                        embedded_dict.pop(key)
                embedded_list.append(embedded_dict)
            return_data = embedded_list
        else:
            embedded_dict = obj.embedded_field
            for key in list(embedded_dict.keys()):
                if key.startswith('_'):
                    embedded_dict.pop(key)
            return_data = embedded_dict
        return return_data

class MovieGroupSerializer(serializers.ModelSerializer): 
    class Meta: 
        model=MovieGroup
        fields = '__all__'

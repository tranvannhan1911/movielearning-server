from rest_framework import serializers
from ..models import Movie,Translate
# ,Subs

# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Movie
#         fields='__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

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

# class SubsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Subs
#         fields='__all__'

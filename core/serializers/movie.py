from rest_framework import serializers
from rest_framework_simplejwt import serializers as serializers_jwt
from core.models import Movie,MovieManager,HierarchyTree
from core.serializers import ResponeSerializer

class MovieSerializer(serializers.Serializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieManager
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HierarchyTree
        fields = '__all__'
        read_only_fields = ('type', 'level',)

    def create(self, validated_data):
        category = super().create(validated_data)
        level = 0
        if category.parent != None:
            level = category.parent.level + 1
        category.level = level
        category.type = "product"
        category.save()
        return category

class WatchMovieSerializer(serializers.ModelSerializer):
    movie_groups = MovieManagerSerializer(read_only=True, many=True, required=False)
    product_category = CategorySerializer(read_only=True)
    # units = UnitExchangeSerializer(source="unitexchanges", read_only=True, many=True)
    units = serializers.SerializerMethodField()
    stock = serializers.IntegerField(read_only=True)
    class Meta:
        model = Movie
        fields ='__all__'


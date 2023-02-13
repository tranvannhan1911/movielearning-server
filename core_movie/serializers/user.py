from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta: 
        model = User 
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only':'true'}
        }
    def create(self, validated_data):
        u = User(**validated_data)
        u.set_password(validated_data['password'])
        u.save()
        return u     
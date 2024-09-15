from rest_framework import serializers
from . models import Movies
class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

        def create(self, validated_data):
            return Movies.objects.create(**validated_data)


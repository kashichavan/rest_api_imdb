from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    rating=serializers.FloatField()
    desc=serializers.CharField()
    

    def create(self,data):
        name=data.pop('name')
        obj,created=Movie.objects.get_or_create(name=name,defaults=data)
        return obj
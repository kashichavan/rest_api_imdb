from rest_framework import serializers
# from .models import Movie

# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     rating=serializers.FloatField()
#     desc=serializers.CharField()


#     # def validate_name(self, name):

#     #     if len(name)<3:
#     #         raise serializers.ValidationError("length should be greather than 3 ")
        
#     #     return name
    

#     def validate(self, attrs):
#         name=attrs.get('name')
#         if len(name)<3:
#             raise serializers.ValidationError("name length should be greather than 3 ")
        
#         return attrs
    

#     def create(self,data):
#         name=data.pop('name')
#         obj,created=Movie.objects.get_or_create(name=name,defaults=data)
#         return obj
    

#     def update(self,instance,data):
#         for k,v in data.items():
#             setattr(instance,k,v)
        
#         instance.save()
#         return instance
    
    
    

# ModelSerializers

# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Movie
#         fields='__all__'

#     def validate_name(self, name):

#         if len(name)<3:
#              raise serializers.ValidationError("length should be greather than 3 ")
#         return name
    

from .models import  *
class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields='__all__'


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model=People
        fields='__all__'
        



class MovieCasteSerializer(serializers.ModelSerializer):
    movie=MoviesSerializer()
    people=PeopleSerializer()

    class Meta:
        model=Movie_Cast
        fields=['movie','people','character_name']



class MovieCastSerializer(serializers.ModelSerializer):
    people = PeopleSerializer(read_only=True)

    class Meta:
        model = Movie_Cast
        fields = ['people', 'character_name']


class MovieActorsSerializer(serializers.ModelSerializer):
    casts=MovieCastSerializer(many=True,read_only=True)

    class Meta:
        model=Movies
        fields=['id', 'title', 'description', 'release_date', 'casts']


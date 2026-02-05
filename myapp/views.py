from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer
# Create your views here.

@api_view(["GET"])
def details_movies(request):
    movies=Movie.objects.all()
    res=MovieSerializer(movies,many=True)
    print(res.data)
    return Response(data=res.data)


@api_view(["GET"])
def detail_movie(request,id):
    movie=Movie.objects.get(id=id)
    res=MovieSerializer(movie)
    print(res.data)
    return Response(data=res.data)



@api_view(["POST"])
def insert_movie(request):
    if request.method=='POST':
        is_list=type(request.data) is list
        s=MovieSerializer(data=request.data,many=is_list)
        if s.is_valid():
            s.save()
        else:
            print(s.data)

        return Response(s.data)
    
    return Response({"info":"you need to insert data"})
    






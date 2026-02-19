from django.shortcuts import render
#from .models import Movie
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from .serializers import MovieSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


# Create your views here.

# @api_view(["GET"])
# def details_movies(request):
#     movies=Movie.objects.all()
#     res=MovieSerializer(movies,many=True)
#     print(res.data)
#     return Response(data=res.data,status=status.HTTP_200_OK)


# @api_view(["GET"])
# def detail_movie(request,id):
#     movie=get_object_or_404(Movie,id=id)
#     res=MovieSerializer(movie)
#     print(res.data)
#     return Response(data=res.data,status=status.HTTP_200_OK)



# @api_view(["POST"])
# def insert_movie(request):
#     if request.method=='POST':
#         is_list=type(request.data) is list
#         s=MovieSerializer(data=request.data,many=is_list)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

        
    
#     return Response({"info":"you need to insert data"},status=status.HTTP_405_METHOD_NOT_ALLOWED)



# @api_view(['PUT','PATCH'])
# def update_view(request,id):
#     obj=Movie.objects.get(id=id)
#     info=request.data
#     is_patch=True if request.method == "PATCH" else False
#     ser=MovieSerializer(instance=obj,data=info,partial=is_patch)
#     if ser.is_valid():
#         ser.save()
#         return Response(data=ser.data,status=status.HTTP_200_OK)

#     return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def delete_view(request,id):
#     obj=get_object_or_404(Movie,id=id)
#     obj.delete()
#     return Response({"info":"object is deleteed"},status=status.HTTP_204_NO_CONTENT)









# class MovieAPIView(APIView):

#     def get(self,request):
#         objs=Movie.objects.all()
#         serializ=MovieSerializer(objs,many=True)
#         return Response(serializ.data,status=status.HTTP_200_OK)
    

#     def post(self,request):
#         datas=request.data
#         is_list=isinstance(datas,list)
#         des=MovieSerializer(data=datas,many=is_list)
#         if des.is_valid():
#             des.save()
#             return Response(des.data,status=status.HTTP_201_CREATED)
        
#         return Response(des.errors,status=status.HTTP_400_BAD_REQUEST)
    


# class MovieDetailView(APIView):

#     def get(self,request,id):
#         obj=get_object_or_404(Movie,id=id)
#         ser=MovieSerializer(obj)
#         return Response(ser.data,status=status.HTTP_200_OK)

#     def put(self,request,id):
#         obj=get_object_or_404(Movie,id=id)
#         datas=request.data
#         ser=MovieSerializer(instance=obj,data=datas)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data,status=status.HTTP_200_OK)

#         return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        

#     def patch(self,request,id):
#         obj=get_object_or_404(Movie,id=id)
#         datas=request.data
#         ser=MovieSerializer(instance=obj,data=datas,partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data,status=status.HTTP_200_OK)

#         return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,id):
#         obj=get_object_or_404(Movie,id=id)
#         obj.delete()
#         return Response({"object":"it has been deleted"},status=status.HTTP_204_NO_CONTENT)


    

# class MovieCreateAPI(GenericAPIView):
#     serializer_class=MovieSerializer
#     queryset=Movie.objects.all()

#     def get(self,request):
#         movies=self.get_queryset()
#         s=self.get_serializer(movies,many=True)
#         return Response(s.data,status=status.HTTP_200_OK)
    
#     def post(self,request):
#         data=request.data
#         s=self.get_serializer(data=data)
#         s.is_valid(raise_exception=True)
#         s.save()
#         return Response(s.data,status=status.HTTP_201_CREATED)




from rest_framework import generics
# class MovieCreate(generics.CreateAPIView):
#     serializer_class=MovieSerializer


# class ReadMovie(generics.ListAPIView):
#     queryset=Movie.objects.all()
#     serializer_class=MovieSerializer


# class MoviesGeneric(generics.ListCreateAPIView):
#     queryset=Movie.objects.all()
#     serializer_class=MovieSerializer


    # def get(self,request):
    #     objs=Movie.objects.filter(rating__gt=9)
    #     s=self.get_serializer(objs,many=True)
    #     return Response(s.data)



# class MovieObject(generics.RetrieveAPIView):
#     queryset=Movie.objects.all()
#     serializer_class=MovieSerializer


# class MovieObject(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Movie.objects.all()
#     serializer_class=MovieSerializer



    # mixins --> class 

# from rest_framework  import mixins 

# class MovieAPI(mixins.CreateModelMixin,generics.GenericAPIView,mixins.ListModelMixin):
#     serializer_class=MovieSerializer
#     queryset=Movie.objects.all()


#     def get_serializer(self, *args, **kwargs):
#         is_list=isinstance(self.request.data,list)
#         if is_list:
#             kwargs['many']=True
#         return super().get_serializer(*args, **kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
    

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    

# class MovieDetailAPI(mixins.RetrieveModelMixin,generics.GenericAPIView,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin
#                     ):
    
#     serializer_class=MovieSerializer
#     queryset=Movie.objects.all()

#     lookup_field='id'

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

#     def patch(self,request,*args,**kwargs):
#         return self.partial_update(request,*args,**kwargs) 

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)   

# from rest_framework import viewsets
# class MovieAPi(viewsets.ModelViewSet):
    
#     serializer_class=MovieSerializer
#     queryset=Movie.objects.all()
#     lookup_field='id'


#     def get_serializer(self, *args, **kwargs):
#         is_list=isinstance(self.request.data,list)
#         if is_list:
#             kwargs['many']=True
#         return super().get_serializer(*args, **kwargs)

from rest_framework import viewsets
from .serializers import *
from .models import *
class MovieCreateAPI(viewsets.ModelViewSet):
    serializer_class=MoviesSerializer
    queryset=Movies.objects.all()
    
    def get_serializer(self, *args, **kwargs):
        is_list=isinstance(self.request.data,list)
        if is_list:
            kwargs['many']=True
        return super().get_serializer(*args, **kwargs)
    
    
class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class=PeopleSerializer
    queryset=People.objects.all()



    def get_serializer(self, *args, **kwargs):
        is_list=isinstance(self.request.data,list)
        if is_list:
            kwargs['many']=True
        return super().get_serializer(*args, **kwargs)
    

# @api_view(['GET'])
# def get_movie_details(request):
#     movies = Movies.objects.all()
#     result = []

#     for movie in movies:
#         casts = Movie_Cast.objects.filter(movie=movie)
#         people = [cast.people for cast in casts]

#         data = {
#             "id": movie.id,
#             "title": movie.title,
#             "description": movie.description,
#             "release_date": movie.release_date,
#             "people": people
#         }

#         serializer = MovieActors(data)
#         result.append(serializer.data)

#     return Response(result)




@api_view(['GET'])
def get_movie_details(request):
    movies = Movies.objects.prefetch_related('casts__people')
    serializer = MovieActorsSerializer(movies, many=True)
    return Response(serializer.data)

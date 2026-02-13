from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer
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









class MovieAPIView(APIView):

    def get(self,request):
        objs=Movie.objects.all()
        serializ=MovieSerializer(objs,many=True)
        return Response(serializ.data,status=status.HTTP_200_OK)
    

    def post(self,request):
        datas=request.data
        des=MovieSerializer(data=datas)
        if des.is_valid():
            des.save()
            return Response(des.data,status=status.HTTP_201_CREATED)
        
        return Response(des.errors,status=status.HTTP_400_BAD_REQUEST)
    


class MovieDetailView(APIView):

    def get(self,request,id):
        obj=get_object_or_404(Movie,id=id)
        ser=MovieSerializer(obj)
        return Response(ser.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        obj=get_object_or_404(Movie,id=id)
        datas=request.data
        ser=MovieSerializer(instance=obj,data=datas)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)

        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def patch(self,request,id):
        obj=get_object_or_404(Movie,id=id)
        datas=request.data
        ser=MovieSerializer(instance=obj,data=datas,partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)

        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        obj=get_object_or_404(Movie,id=id)
        obj.delete()
        return Response({"object":"it has been deleted"},status=status.HTTP_204_NO_CONTENT)


    


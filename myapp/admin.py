from django.contrib import admin
# from .models import Movie
# Register your models here.

# class MovieAdmin(admin.ModelAdmin):
#     list_display=['id','name','desc','rating']

# admin.site.register(Movie,MovieAdmin)



from myapp.models import *


class MoviesAdmin(admin.ModelAdmin):
    list_display=['id','title','description','release_date']



class  MovieCastAdmin(admin.ModelAdmin):
    list_display=['movie','people','character_name']


admin.site.register(Movie_Cast,MovieCastAdmin)


admin.site.register(Movies,MoviesAdmin)

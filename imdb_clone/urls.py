"""
URL configuration for imdb_clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from myapp.views import details_movies,detail_movie,insert_movie,update_view,
#from myapp.views import MovieAPIView,MovieDetailView
from myapp.views import *

from rest_framework import routers

router=routers.DefaultRouter()

router.register("detail",MovieAPi)



urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('details/',details_movies),
    # path('details/<int:id>/',detail_movie),
    # path('insert/',insert_movie),
    # path('update/<int:id>/',update_view)

    # path('details/',MovieAPIView.as_view(),name='details'),
    # path('detail/<int:id>',MovieDetailView.as_view(),name="detail")

    #path('details/',MoviesGeneric.as_view()),

    #path('get_details/',ReadMovie.as_view())

    path("",include(router.urls))
   

]




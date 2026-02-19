from django.db import models

# Create your models here.

# class Movie(models.Model):
#     name=models.CharField(max_length=25)
#     rating=models.FloatField()
#     desc=models.CharField(max_length=100)



class Movies(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    release_date=models.DateTimeField()

    def __str__(self):
        return self.title


class People(models.Model):
    name=models.CharField(max_length=30)


    def __str__(self):
        return self.name



class Movie_Cast(models.Model):
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE,related_name='casts')
    people=models.ForeignKey(People,on_delete=models.CASCADE,related_name='casts')
    character_name=models.CharField(max_length=30)

    

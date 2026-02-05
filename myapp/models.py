from django.db import models

# Create your models here.

class Movie(models.Model):
    name=models.CharField(max_length=25)
    rating=models.FloatField()
    desc=models.CharField(max_length=100)



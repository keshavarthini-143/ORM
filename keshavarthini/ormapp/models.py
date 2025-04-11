from django.db import models
from django.contrib import admin
class Movie (models.Model):
    mid=models.IntegerField()
    mname=models.CharField(max_length=100)
    collection=models.IntegerField()
    year=models.IntegerField()
    rating=models.FloatField(max_length=10.0)


class MovieAdmin(admin.ModelAdmin):
    list_display=('mid', 'mname', 'collection', 'year', 'rating')
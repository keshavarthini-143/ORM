# Ex02 Django ORM Web Application
## Date: 11.04.2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from.models import Movie,MovieAdmin
admin.site.register(Movie,MovieAdmin)

models.py


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
```

## OUTPUT

![Screenshot 2025-04-11 114631](https://github.com/user-attachments/assets/de464d1a-08ab-45d1-ac3b-6d52f8e8e823)


## RESULT

Thus the program for creating movies database using ORM hass been executed successfully




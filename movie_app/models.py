from django.db import models
from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=20)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)


class Review(models.Model):
    text = models.TextField(max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=20)

    @property
    def movie_count(self):
        return self.movies.all().count()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE,related_name='movies')

    @property
    def rating(self):
        count = self.reviews.count()
        if count == 0:
            return 0
        total = 0
        for i in self.reviews.all():
            total += i.stars
        return total / count

    def __str__(self):
        return self.title

    @property
    def director_name(self):
        return self.director.name


class Review(models.Model):
    text = models.TextField(max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', null=True)
    stars = models.IntegerField(choices=([i, i * '*'] for i in range(1, 6)), default=0)

    def __str__(self):
        return self.text

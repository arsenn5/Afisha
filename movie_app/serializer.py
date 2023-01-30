from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movie_count'.split()

    def get_movie_count(self, director):
        return director.movie_count


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer().fields.get("name")

    class Meta:
        model = Movie
        fields = 'id title description duration director rating'.split()


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie'.split()


class MovieReviewSerializer(serializers.ModelSerializer):
    director = DirectorSerializer().fields.get("name")
    reviews = ReviewsSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "id title description duration director rating reviews".split()

    def get_reviews(self, movie):
        return [i.stars for i in movie.reviews.all()]

    def get_rating(self, movie):
        return movie.rating


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars movie'.split()


class MovieValidationSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1)
    description = serializers.CharField()
    duration = serializers.FloatField(max_value=6.0)
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError(f'Director with ({director_id}) does not exists!')
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField(max_value=5)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError(f'Movie with ({movie_id}) does not exists!')
        return movie_id


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField()
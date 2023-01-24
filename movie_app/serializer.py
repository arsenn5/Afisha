from rest_framework import serializers

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
        fields = 'id text stars'.split()
        tag_list = serializers.SerializerMethodField()


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
        fields = 'id movie'.split()

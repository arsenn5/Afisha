from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie_app.serializer import *
from .models import *


@api_view(['GET'])
def directors_view(request):
    director = Director.objects.all()
    serializer = DirectorSerializer(director, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(director, many=False)
    return Response(data=serializer.data)


@api_view(["GET"])
def movie_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Review not found!'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def reviews_view(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieReviewSerializer(movie, many=True)
        return Response(data=serializer.data)


@api_view(['GET'])
def test(request):
    data = {
        'text': 'Hello world',
        'int': 1000,
        'float': 123.234,
        'list': [1, 123, 123]
    }
    return Response(data=data)

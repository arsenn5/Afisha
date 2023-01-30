from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie_app.serializer import *
from .models import *


@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        serializer = DirectorSerializer(director, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        name = serializer.validated_data.get('name')
        director = Director.objects.create(name=name)
        director.save()
        return Response(data={'massage':'data received'})


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(director, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        director.name = serializer.validated_data.get('name')
        director.save()
        return Response(data={'massage': 'data received'})


@api_view(["GET", 'POST'])
def movie_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = MovieValidationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        # # movie.director.set(director)
        movie.save()
        return Response(data={'massage': 'data received'})


@api_view(["GET", "PUT", "DELETE"])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = MovieValidationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director_id')
        # # movie.director.set(director)
        movie.save()
        return Response(data={'massage': 'data received'})


@api_view(['GET', 'POST'])
def review_view(request):
    review = Review.objects.all()
    if request.method == 'GET':
        serializer = ReviewSerializer(review, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id', 6)
        review = Review.objects.create(text=text, stars=stars, movie_id=movie_id)
        review.save()
        return Response(data={'massage': 'data received'})


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Review not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie_id = request.data.get('movie_id', 6)
        review.save()
        return Response(data={'massage': 'data received'})


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
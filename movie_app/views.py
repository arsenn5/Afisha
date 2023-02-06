from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from movie_app.serializer import *
from .models import *


class DirectorListAPIView(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


class MovieAPIView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        serializer = MovieValidationSerializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        movie = Movie.objects.create(**serializer.validated_data)
        # # movie.director.set(director)
        movie.save()
        return Response(data={'massage': 'data received'})


class ReviewAPIView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        review = Review.objects.create(**serializer.validated_data)
        review.save()
        return Response(data={'massage': 'data received'})


class MovieReviewAPIView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer
    lookup_field = "id"
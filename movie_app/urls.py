from django.urls import path

from movie_app import views

list_create = {
    'get': 'list',
    'post': 'create'}

update_retrieve_destroy = {
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'}

urlpatterns = [
    path('directors/', views.DirectorListAPIView.as_view(list_create)),
    path('directors/<int:id>', views.DirectorListAPIView.as_view(update_retrieve_destroy)),
    path('movie/', views.MovieAPIView.as_view(list_create)),
    path('movie/<int:id>', views.MovieAPIView.as_view(update_retrieve_destroy)),
    path('movie/review/', views.MovieReviewAPIView.as_view(list_create)),
    path('movie/review/<int:id>', views.MovieReviewAPIView.as_view(update_retrieve_destroy)),
    path('review/', views.ReviewAPIView.as_view(list_create)),
    path('review/<int:pk>', views.ReviewAPIView.as_view(update_retrieve_destroy)),
]

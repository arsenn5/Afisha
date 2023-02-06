from django.urls import path
from . import views
urlpatterns = [
    path('authorization/', views.AuthorizationCreateAPIView.as_view()),
    path('registration/',views.RegistrationCreateAPIView.as_view())
]
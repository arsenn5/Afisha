from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from users.serializer import UserValidateSerializer, UserCreateSerializer
from django.contrib.auth.models import User

@api_view(['POST'])
def registration_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    User.objects.create_user(**serializer.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def authorization_view(request):
    serializer = UserValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(username=serializer.validated_data.get('username'),
                        password=serializer.validated_data.get('password'))
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'token': token.key})
    return Response(status=status.HTTP_403_FORBIDDEN,
                    data={'errors_massage': 'user not found'})



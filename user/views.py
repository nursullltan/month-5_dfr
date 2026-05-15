from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import UserConfirm
from .serializer import UserRegistrationSerializer, UserConfirmSerializer
from rest_framework import status
# Create your views here.
@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()
    
    return Response (data={'user_id':user.id, 'massange': 'Пользователь создан! проверьте терминал для кода'}, 
                     status=status.HTTP_201_CREATED)


@api_view(['POST'])
def confirm_api_view(request):
    serializer = UserConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    code = serializer.validated_data.get('code')

    try:
        confirmation = UserConfirm.objects.get(user__username=username, code=code)
        user = confirmation.user
        user.is_active = True
        user.save()
        confirmation.delete() 
        
        return Response(data={'message': 'Успешный вход'}, status=status.HTTP_200_OK)
    except UserConfirm.DoesNotExist:
        return Response(data={'error': 'Не правильный код или имя'}, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.shortcuts import render
from .models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# def user_list(request):
#     users = CustomUser.objects.all()
#     return render(request, 'users/user_list.html', {'users': users})

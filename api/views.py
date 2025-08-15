from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from photo_gallery_app.models import Photo_Gallery
from django.contrib.auth.models import User

# Create your views here.

@api_view(['POST'])
def api_add_photos(request,username):
    if User.objects.get(username=username).is_authenticated:
        serializer = PhotoSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','DELETE'])
def api_photo_list(request,username,pk):
    pass
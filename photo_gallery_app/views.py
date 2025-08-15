
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from random import choice
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@login_required
def home(request):
    context = {
        'user':request.user,
        'photos':Photo_Gallery.objects.all(),
    }
    
    return render(request, 'index.html', context)

def photo(request,username,pk):
    context = {
        'photo':None,
        'previous_url':None
    }
    previous_url = request.META.get('HTTP_REFERER')
    try:
        photo = Photo_Gallery.objects.get(pk=pk)
    except Photo_Gallery.DoesNotExist:
        return redirect('home')
    context['photo']=photo
    context['previous_url'] = previous_url if previous_url else None
    return render(request,'photo.html',context)


def add_photo(request):
    context = {}
    return render(request,'add_photo.html',context)

def user_profile(request,username):
    context = {

    }
    if not  User.objects.filter(username=username).exists():
        return redirect('home')
    return render(request, 'user_profile.html')
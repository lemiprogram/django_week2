
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from random import choice
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.views import *
from requests import post
from .forms import *
from api.serializers import *

@login_required
def home(request):
    # Show all photos ordered by newest first
    context = {
    'photos':Photo.objects.all()

    }
    return render(request, 'index.html', context)

@login_required
def photo(request,pk):
    context = {
        'photo':None,
        'previous_url':None
    }
    previous_url = request.META.get('HTTP_REFERER')
    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        return redirect('home')
    context['photo']=photo
    context['previous_url'] = previous_url if previous_url else None
    return render(request,'photo.html',context)


@login_required
def add_photo(request):
    context = {}
    if request.method == 'POST':
        photo = PhotoUploadForm(request.POST)
        photo.user = request.user
        if photo.is_valid():
            photo.save()
            return redirect('home')
        else:
            context['erros'] = photo.errors
    return render(request,'add_photo.html',context)

@login_required
def user_profile(request,username):
    context = {

    }
    if not  User.objects.filter(username=username).exists():
        return redirect('home')
    return render(request, 'user_profile.html')
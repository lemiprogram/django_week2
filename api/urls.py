
from django.urls import path
from .views import *
urlpatterns = [
    path('<str:username>/add_photo', api_add_photos, name='api_add_photos'),
    path('<str:username>/photo_list/<int:pk>', api_photo_list, name='api_add_photos'),
]

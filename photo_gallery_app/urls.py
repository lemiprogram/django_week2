
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('add_photo/', add_photo, name='add_photo'),
    
]
                        
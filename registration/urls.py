from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView    
from django.conf import settings
urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_out/', sign_out, name='sign_out'),
]
                        
from django.contrib.postgres.fields import ArrayField
from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Photo_Gallery(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32,default="Photo image" )
    photo = CloudinaryField('image', blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=16), size=None,blank=True, null=True )
    

    def __str__(self):
        return self.title

class User_Details(models.Model):
    name = models.CharField(max_length=64,default='', null=True)
    bio = models.CharField(max_length=256, default='', null=True)
    profile_photo = CloudinaryField('image',blank=True, null=True)

    
    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.postgres.fields import ArrayField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = CloudinaryField('image', folder='profile_pics', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Photo(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='photos')
    image = CloudinaryField('image', folder='gallery')
    caption = models.CharField(max_length=255, blank=True)
    tags = ArrayField(models.CharField(max_length=32, blank=True, null=True))
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo by {self.profile.user.username}"

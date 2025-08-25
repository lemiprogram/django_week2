from rest_framework import serializers
from photo_gallery_app.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Photo
        fields = '__all__'
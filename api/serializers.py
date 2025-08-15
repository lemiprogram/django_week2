from rest_framework import serializers
from photo_gallery_app.models import Photo_Gallery


class PhotoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Photo_Gallery
        fields = '__all__'
from django import forms
from .models import Photo_Gallery as Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'title', 'description'] 
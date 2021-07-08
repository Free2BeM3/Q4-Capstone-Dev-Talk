from django import forms
from uploads.models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=('caption', 'image')

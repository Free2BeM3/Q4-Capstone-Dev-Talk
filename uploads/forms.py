from django import forms
from uploads.models import Image, Comment 

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=['caption', 'image']

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =[
            "body"
        ]

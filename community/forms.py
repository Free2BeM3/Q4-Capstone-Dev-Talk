from django import forms
from community.models import CommunityImage, CommunityComment


class CIForm(forms.ModelForm):
    class Meta:
        model = CommunityImage
        fields = ['caption', 'image']


class RespondForm(forms.ModelForm):
    class Meta:
        model = CommunityComment
        fields = [
            "body"
        ]

from django import forms
from django.forms import fields
from custom_users.models import Uzer


class SignupForm(forms.ModelForm):
    class Meta:
        model = Uzer
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Uzer
        fields = [
            'avatar',
            'bio',
            'location',
            'github',
            'linkedin',
            'portfolio'
            
        ]
from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField

    class Meta:
        model = User
        fields = [
            'username'
            'email'
            'password'
        ]
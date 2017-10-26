from django import forms
from .models import Post, User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User

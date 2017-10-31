from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserLoginForm(UserCreationForm):
    username = forms.CharField(help_text=' xdd')
    email = forms.EmailField(help_text='lollll')


    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
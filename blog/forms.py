from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserLoginForm(UserCreationForm):
    username = forms.CharField(help_text=' xdd')
    email = forms.EmailField(help_text='lollll')
    #override good ! :D :D coz default is broken xdd
    password1 = forms.CharField(help_text='lalalallala')


    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
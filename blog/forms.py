from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(UserCreationForm):
    username = forms.CharField(help_text=' xdd')
    email = forms.EmailField(help_text='lollll')
    #overriden UserCreationForm help texts coz lazy


    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

class UserLoginFormLegit(AuthenticationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )
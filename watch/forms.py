from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import User_profile, Neighborhood, Bussiness
from django.forms.widgets import PasswordInput, TextInput



class SignUpForm(UserCreationForm):
    """ form for generating the user """
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class LoginForm(AuthenticationForm):
    """ form for login """
    username = forms.CharField(widget=TextInput(
        attrs={'class': 'validate', 'placeholder': ' Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': ' Password'}))

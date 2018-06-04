from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import User_prof, Neighborhood, Bussiness,Posts
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

class UserProfForm(forms.ModelForm):
    """updating user infomation """
    class Meta:
        model = User_prof
        fields = ( 'phone_num')
        exclude = ('user', 'mail-confirm', 'user_location')

class PostForm(forms.ModelForm):
    """ form for posting some infmation """
    comment = forms.CharField(help_text="Please enter some text.") 
    class Meta:
        model = Posts
        fields = ('title', 'comment')
        exclude = ('user_name',)

class NeighborhoodForm(forms.ModelForm):
    """ form for adding infomation to the neighboorhood class"""
    name = forms.CharField(help_text="Please enter the name of the neighborhood.")
    location = forms.CharField(help_text="Please enter the location.")
    occupant_count = forms.IntegerField(widget=forms.HiddenInput(), initial=0)


    class Meta:
        model = Neighborhood
        fields = ( 'name', 'location', 'occupant_count')

class BusinessForm(forms.ModelForm):
    """form for adding infomation to the bussiness class  """
    bussiness_name = forms.CharField(help_text="Please enter the name of the business.")
    Email_adress = forms.CharField(required=False, help_text="Enter the business's email address.")

    class Meta:
        model = Business
        fields = ('bussiness_name', 'Email_adress')
        exclude = ('neighborhood','user')


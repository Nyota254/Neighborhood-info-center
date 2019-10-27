from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from main.models import Neighborhood

class UserRegisterForm(UserCreationForm):
    '''
    Form to register users
    '''
    email = forms.EmailField()
    neighborhood = forms.ModelChoiceField(queryset=Neighborhood.objects.all())
    class Meta:
        model = User
        fields = ["username","email","neighborhood","password1","password2"]

class UserUpdateForm(forms.ModelForm):
    '''
    Form to update user profile
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    '''
    Form to update user profile picture
    '''
    neighborhood = forms.ModelChoiceField(queryset=Neighborhood.objects.all())
    class Meta:
        model = Profile
        fields = ['bio','neighborhood','profile_picture']


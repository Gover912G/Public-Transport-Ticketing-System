
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Profile
from  django.forms import ModelForm

class PassengerRegistrationForm(UserCreationForm):
    # first_name= forms.CharField(max_length= 50)
    # last_name= forms.CharField(max_length= 50)
    # phone_number = forms.CharField(max_length=15)
    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]


class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        fields='__all__'
        exclude = ['user']
      
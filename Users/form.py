
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class PassengerRegistrationForm(UserCreationForm):
    first_name= forms.CharField(max_length= 50)
    last_name= forms.CharField(max_length= 50)
    phone_number = forms.CharField(max_length=15)
    class Meta:
        model = User
        fields = ["first_name", "last_name",'username', 'email','phone_number', 'password1', 'password2']
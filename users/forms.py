from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

# TO WORK ON PROFILE MODEL WE HAVE TO IMPORT THAT 
from .models import Profile



# this is to add additional feilds by inheriting the UserCreationForm 
class UserRegisterForm(UserCreationForm):
    # here required=true is by default 
    email= forms.EmailField()


    # this will tell to which model we is to interact with 
    class Meta:
        model=User
        fields=['username','email','password1','password2']


# this form is to update user model 
class UserUpdateForm(forms.ModelForm):
    # here required=true is by default 
    email= forms.EmailField()


    # this will tell to which model we is to interact with 
    class Meta:
        model=User
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']



from django import forms

from .models import CustomUsers

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()



class CustomUserForm(UserCreationForm):
    class Meta:
        model=CustomUsers
        fields="__all__"

class RegistrationForm(UserCreationForm):
        username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','maxlength':"20",'title':'Ener charactors only','required':'true'}))
        first_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'FirstName','maxlength':"20",'title':'Ener charactors only','required':'true'}))
        email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','autofocus':'autofocus','required':'true'}))
        password1= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','maxlength':"20",'required':'true'}))
        password2= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password','maxlength':"20",'required':'true'}))
        user_photo= forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'User Photo','accept':'image/'}))

        class Meta:
            model= CustomUsers
            fields= ('username','first_name','email','password1','password2','user_photo')
            #fields='__all__'


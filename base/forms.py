from ast import Add
from .models import AddFood
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class AddFoodForm(ModelForm):
    class Meta:
        model = AddFood
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'label',
        'for':'user',
        'id':'user',
        'type':'text',
        'class':'input'
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'label',
        'for':'pass',
        'id':'pass',
        'type':'password',
        'class':'input'

        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'label',
        'for':'pass',
        'id':'pass',
        'type':'password',
        'class':'input'

        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'label',
        'for':'pass',
        'id':'pass',
        'type':'email',
        'class':'input'
        }))
    class Meta:
        model = User    
        fields = ['username','email','password1','password2']
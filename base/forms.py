from ast import Add
from .models import AddFood
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AddFoodForm(ModelForm):
    class Meta:
        model = AddFood
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User    
        fields = ['username','email','password1','password2']
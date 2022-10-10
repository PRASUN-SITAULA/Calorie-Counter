from ast import Add
from .models import AddFood
from django.forms import ModelForm
from django.contrib.auth.models import User

class AddFoodForm(ModelForm):
    class Meta:
        model = AddFood
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
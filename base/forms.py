from ast import Add
from .models import AddFood
from django.forms import ModelForm

class AddFoodForm(ModelForm):
    class Meta:
        model = AddFood
        fields = '__all__'
        # exclude = ('calorie_goal')

# class AddFoodLunchForm(ModelForm):
#     class Meta:
#         model = AddFoodLunch
#         fields = '__all__'

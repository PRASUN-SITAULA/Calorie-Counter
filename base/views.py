from ast import Add
import re
from django.shortcuts import render, redirect
from .forms import AddFoodForm, CustomUserCreationForm
from django.contrib import messages
from .models import AddFood
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    food_details = AddFood.objects.all()
    calories_consumed = []
    protein_consumed = []
    fats_consumed = []
    carbs_consumed = []
    for calories in food_details:
        calories_consumed.append(calories.calorie)   # add calories value in list
        protein_consumed.append(calories.protein)   # add protein value in list
        fats_consumed.append(calories.fats)         # add fats value in list
        carbs_consumed.append(calories.carbs)        # add carbs value in list

    total_calories,total_protein,total_fats,total_carbs = 0,0,0,0
    for c,p,f,b in zip(calories_consumed, protein_consumed,fats_consumed,carbs_consumed):
        total_calories += c
        total_protein += p
        total_fats += f
        total_carbs += b
        
    context = {
        'food_details': food_details, 
        'total_calories': total_calories,
        'total_protein': total_protein,
        'total_fats': total_fats,
        'total_carbs': total_carbs,
    }
    return render(request, 'base/home.html', context)

def add_food(request):
    form =AddFoodForm()
    if request.method == "POST":          # if the form has been submitted
        form = AddFoodForm(request.POST)
        if form.is_valid():                # checks if the form is valid or not
            form.save()
            return redirect(home)
        else:
            messages.error(request, "An error occurred!")
    return render(request, 'base/add_food.html', {'form': form})


def details(request):
    food_details = AddFood.objects.all()
    calories_consumed = []
    protein_consumed = []
    fats_consumed = []
    carbs_consumed = []
    for calories in food_details:
        calories_consumed.append(calories.calorie)   # add calories value in list
        protein_consumed.append(calories.protein)   # add protein value in list
        fats_consumed.append(calories.fats)         # add fats value in list
        carbs_consumed.append(calories.carbs)        # add carbs value in list

    total_calories,total_protein,total_fats,total_carbs = 0,0,0,0
    for c,p,f,b in zip(calories_consumed, protein_consumed,fats_consumed,carbs_consumed):
        total_calories += c
        total_protein += p
        total_fats += f
        total_carbs += b
    context = {
        'food_details': food_details, 
        'total_calories': total_calories,
        'total_protein': total_protein,
        'total_fats': total_fats,
        'total_carbs': total_carbs,
    }
    return render(request, 'base/details.html', context)


def update_food(request, pk):
    food_details = AddFood.objects.get(id=pk)
    form = AddFoodForm(instance=food_details)    #instance => to fetch previous data
    if request.method == "POST":
        form = AddFoodForm(request.POST, instance=food_details)
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            messages.error(request, "An error occurred. Please try again.")    #  flash messsages
     
    return render(request, 'base/update_food.html', {'food_details': food_details, 'form':form})
        
def delete_food(request, pk):
    food_details = AddFood.objects.get(id=pk)   # retrieves data based on id pointed by django
    if request.method == "POST":
        food_details.delete()
        return redirect(home)
    else:
        return render(request, 'base/delete.html', {'food_details': food_details})


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            messages.error(request, "you are not registered.")
    else:
        return render(request, 'base/login.html', {})

def logoutpage(request):
    logout(request)
    return redirect(loginpage)


def registeruser(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(loginpage)
        else:
            messages.error(request,"Failed to register.")
    return render(request, 'base/register.html', {'form':form})
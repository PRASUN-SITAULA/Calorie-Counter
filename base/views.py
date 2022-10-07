from ast import Add
from django.shortcuts import render, redirect
from .forms import AddFoodForm
from django.contrib import messages
from .models import AddFood

# Create your views here.
def home(request):
    calories_consumed = []
    total_calories = 0
    food_detail = AddFood.objects.all()      # query data from the database
    for calories in food_detail:
        calories_consumed.append(calories.calorie)
    for i in calories_consumed:
        total_calories += i
    # lunch_details = AddFoodLunch.objects.all()
    context = {
        'food_detail': food_detail, 
        # 'lunch_details': lunch_details,
        'total_calories': total_calories
        }
    return render(request, 'base/home.html', context)

def add_food(request):
    form =AddFoodForm()
    lunch = AddFoodForm()
    if request.method == "POST":          # if the form has been submitted
        form = AddFoodForm(request.POST)
        # lunch = AddFoodLunchForm(request.POST)
        if 'breakfast' in request.POST:
            if form.is_valid():                # checks if the form is valid or not
                form.save()
                return redirect(home)
            else:
                messages.error(request, "An error occurred!")
        # if 'lunch' in request.POST:
        #     if lunch.is_valid():
        #         lunch.save()
        #         return redirect(home)
        #     else:
        #         messages.error(request, "An error occurred!!")
    return render(request, 'base/add_food.html', {'form': form, 'lunch': lunch})


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
    return render(request, 'base/delete.html', {'food_details': food_details})


from django.db import models

# Create your models here.

class AddFood(models.Model):
    name_of_food = models.CharField(max_length=200)
    calorie = models.IntegerField()
    protein = models.DecimalField(default=0,max_digits=20,decimal_places=4)
    fats = models.DecimalField(default=0,max_digits=20,decimal_places=4)
    carbs = models.DecimalField(default=0,max_digits=20,decimal_places=4)
    # calorie_goal = models.PositiveBigIntegerField(default=0)

    def __str__(self):
       return self.name_of_food


# class AddFoodLunch(models.Model):
#     name_of_food = models.CharField(max_length=200)
#     calorie = models.IntegerField()
#     protein = models.DecimalField(max_digits=20,decimal_places=4)
#     fats = models.DecimalField(max_digits=20,decimal_places=4)
#     carbs = models.DecimalField(max_digits=20,decimal_places=4)

#     def __str__(self):
#         return self.name_of_food

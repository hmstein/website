from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=3000)
    description = models.CharField(max_length=3000)
    created_dttm = models.DateTimeField(auto_now_add=True)

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, null=False, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    step_num = models.FloatField()

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit_type = models.CharField(max_length=50)

from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    notes = models.CharField(max_length=3000)
    created_dttm = models.DateTimeField(auto_now_add=True)
    

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE)
    step_num = models.IntegerField()
    text = models.CharField(max_length=500)

    class Meta:
        unique_together = [ 'recipe', 'step_num' ]
        ordering = ['step_num']

    def __str__(self):
        return 'Step #{0}: {1}}'.format(self.step_num, self.text)

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit_type = models.CharField(max_length=50)
    
    class Meta:
        unique_together = ['recipe', 'name']

    def __str__(self):
        return '{0} {1} {2}'.format(self.quantity, self.unit_type, self.name)

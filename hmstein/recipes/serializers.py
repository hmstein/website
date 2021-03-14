from rest_framework import serializers
from .models import Recipe, Ingredient, Step



class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'quantity', 'unit_type']

class StepSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Step
        fields = ['id', 'step_num', 'text']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    steps = StepSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'ingredients', 'steps', 'notes', 'created_dttm']
        read_only_fields = ['id', 'created_dttm']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        steps_data = validated_data.pop('steps')
        recipe = Recipe.objects.create(**validated_data)
        for ingrd in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingrd)
        for step in steps_data:
            Step.objects.create(recipe=recipe, **step)
        return recipe

    def update(self, instance, validated_data):
        ingredients = validated_data.pop('ingredients')
        steps = validated_data.pop('steps')
        
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.notes = validated_data.get("notes", instance.notes)
        instance.save()

        keep_ingredients = []
        keep_steps = []

        for ingrd in ingredients:
            if 'id' in ingrd.keys():
                if Ingredient.objects.filter(id=ingrd['id']).exists():
                    i = Ingredient.objects.get(id=ingrd['id'])
                    i.name = ingrd.get('name', i.name)
                    i.quantity = ingrd.get('quantity', i.quantity)
                    i.unit_type = ingrd.get('unit_type', i.unit_type)
                    i.save()
                    keep_ingredients.append(i.id)
                else:
                    continue
            else:
                i = Ingredient.objects.create(recipe=instance, **ingrd)
                keep_ingredients.append(i.id)

        for ingrd in instance.ingredients.all():
            if ingrd.id not in keep_ingredients:
                ingrd.delete()
            
        for step in steps: 
            if 'id' in step.keys():
                if Step.objects.filter(id=step['id']).exists():
                    s = Step.objects.get(id=step['id'])
                    s.step_num = step.get('step_num', s.step_num)
                    s.text = step.get('text', s.text)
                    s.save()
                    keep_steps.append(s.id)
                else:
                    continue
            else:
                s = Step.objects.create(recipe=instance, **step)
                keep_steps.append(s.id)

        for step in instance.steps.all():
            if step.id not in keep_steps:
                step.delete()

        return instance

from rest_framework import routers
from .api import RecipeViewSet

router = routers.DefaultRouter()
router.register('api/recipes', RecipeViewSet, 'recipes')

urlpatterns = router.urls

"""
from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    path('api-overview', views.apiOverview, name='api-overview'),
    path('', views.getRecipes, name='GET-recipes'),
    path('<str:pk>', views.getRecipe, name='GET-recipe'),
    path('', views.postRecipe, name='POST-recipe'),
    path('<str:pk>', views.putRecipe, name='PUT-recipe'),
    path('<str:pk>', views.deleteRecipe, name='DELETE-recipe'),
]
"""

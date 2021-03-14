from django.contrib import admin
from rest_framework import routers
from django.urls import include, path


urlpatterns = [
    path('', include('home.urls')),
    path('', include('recipes.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]

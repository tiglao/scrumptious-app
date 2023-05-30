from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_recipe_list(request):
    return redirect("recipe_list")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("recipes.urls")),
    path("", redirect_to_recipe_list, name="redirect_to_recipe_list"),
]

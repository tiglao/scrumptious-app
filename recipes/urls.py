from django.urls import path
from recipes.views import show_recipe, recipe_list, create_recipe, edit_recipe


urlpatterns = [
    path("recipes/", recipe_list, name="recipe_list"),
    path('recipes/<int:id>/', show_recipe, name="show_recipe"),
    path("recipes/create/", create_recipe, name="create_recipe"),
    path("recipes/<int:id>/edit/", edit_recipe, name="edit_recipe"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)

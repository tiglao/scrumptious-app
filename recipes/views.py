from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from recipes.forms import RecipeForm

def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "recipe_object": recipe,
    }
    return render(request, "recipes/detail.html", context)

# def recipe_list(request):
#     recipes = get_object_or_404(Recipe)
#     context = {
#         "recipes": recipes,
#     }
#     return render(request, "recipes/list.html", context)

def recipe_list(request):
      recipes = Recipe.objects.all()
      context = {
        "recipe_list": recipes,
      }

      return render(request, "recipes/list.html", context)

#    recipes = Recipe.objects.all()
#    context = {
#        "recipe_list": recipes,
#    }
#    return render(request, "recipes/list.html", context)


def create_recipe(request):
   form = RecipeForm(request.POST)
   if form.is_valid():
      form.save()
      return redirect("recipe_list")
   else:
      form = RecipeForm()
   context = {
      "form": form,
   }

   return render(request, "recipes/create.html", context)

# def create_post(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("posts_list")
#     else:
#         form = PostForm()

#     context = {
#         "post_form": form,
#     }
#     return render(request, "posts/create.html", context)

   # form = RecipeForm(request.POST)
   # if form.is_valid():
   #    form.save()
   #    return redirect("recipe_list")
   # else:
   #    form = RecipeForm()
   # context = {
   #    "form": form,
   # }

   # return render(request, "recipes/create.html", context)

def edit_recipe(request, id):
   recipe = get_object_or_404(Recipe, id=id)
   if request.method == "POST":
      form = RecipeForm(request.POST, instance=recipe)
      if form.is_valid():
         form.save()
         return redirect("recipe_list", id=id)
   else:
      form = RecipeForm(instance=recipe)

   context = {
      "recipe_object": recipe,
      "form": form,
   }

   return render(request, "recipes/edit.html", context)

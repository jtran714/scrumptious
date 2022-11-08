from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm
# Create your views here.


# def show_recipe(request):
#     recipes = Recipe.objects.all() # all the models all recipes
#     context = {
#         "show_recipe": recipes,
#     }
#     return render(request, "recipes/detail.html")

# def show_recipe_list(request):
#     return render(request, "recipes/list.html")

def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id) # if localhost800/recipe/6 itll return 404
    context = {
        "recipe_object": recipe,
    }
    return render(request, "recipes/detail.html", context)


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "show_recipe": recipes,
    }
    return render(request, "recipes/list.html", context)


def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST) # if form is gucci function ends at return
        if form.is_valid():
            form.save()
            return redirect("recipes_list")
    else:
         form = RecipeForm() # if user didn't submit correctly it will return the context which is the blank form
      
         context = {
         "form": form
        }
         return render(request, "recipes/create.html", context)


def edit_recipe(request, id): 
    recipe = Recipe.objects.get(id=id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("show_recipe", id=id)
    else:
        form = RecipeForm(instance=recipe)

        context = {
        "recipe_object": recipe,
        "form": form,
        }
        return render(request, "recipes/edit.html", context)




# def redirect_to_recipe_list(request):
#     return redirect("recipes_list")





#view function gets the data 
#puts the data in a context
#renders the html with that context data
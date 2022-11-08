from django.urls import path
# import show_recipe from views
from recipes.views import show_recipe, recipe_list, create_recipe, edit_recipe

# "recipes" is the URL (localhost:8000/recipes)
# show_recipe is our view function name
urlpatterns = [
    path("<int:id>/", show_recipe, name="show_recipe"),
    path("list.html", recipe_list, name="recipes_list"),
    path("detail.html", show_recipe),
    path("", recipe_list),
    path("list.html", show_recipe),
    path("create/", create_recipe, name="create_recipe"),
    path("<int:id>/edit", edit_recipe, name="edit_recipe")
]


# #name= here to name recipes or whatever

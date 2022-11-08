from tkinter import CASCADE
from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=250)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class RecipeStep(models.Model):
#     instruction = models.TextField(),
#     order = models.PositiveIntergerField(),
#     recipe = models.ForeignKey(
#         "Recipe", 
#         related_name="steps",
#         on_delete=models.CASCADE,
#     )

    # def recipe_title(self):
    #     return self.recipe.title

#     class Meta:
#         ordering = ["order"]
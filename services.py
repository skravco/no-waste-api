from data import RECIPES
from models import Recipe


class RecipeService:
    def __init__(self):
        self.recipes = []
        for recipe_data in RECIPES:
            self.recipes.append(Recipe(**recipe_data))

    def find_recipe_by_ingredient(self, ingredient_name):
        matching_recipes = []
        for recipe in self.recipes:
            if recipe.contains_ingredient(ingredient_name):
                matching_recipes.append(recipe)
        return matching_recipes

    def get_recipe_by_name(self, name):
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                return recipe
        return None

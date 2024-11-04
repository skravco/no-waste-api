class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = []
        for i in ingredients:
            self.ingredients.append(Ingredient(i))

    def to_dict(self):
        ingredients_list = []
        for ingredient in self.ingredients:
            ingredients_list.append(ingredient.name)
        return {
            'name': self.name,
            'ingredients': ingredients_list
        }

    def contains_ingredient(self, ingredient_name):
        for ingredient in self.ingredients:
            if ingredient.name.lower() == ingredient_name.lower():
                return True
        return False


class Ingredient:
    def __init__(self, name):
        self.name = name

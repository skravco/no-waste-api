import os
from flask import Flask, jsonify, request
from flask_cors import CORS # import CORS
from services import RecipeService

app = Flask(__name__)
CORS(app) # enable CORS for all routes
recipe_service = RecipeService()


@app.route('/recipes', methods=['GET'])
def get_recipes_by_ingredient():
    ingredient = request.args.get('ingredient')
    if not ingredient:
        return jsonify(
            {'error': 'ingredient parameter is required!'}), 400

    recipes = recipe_service.find_recipe_by_ingredient(ingredient)
    recipes_dict_list = []
    for recipe in recipes:
        recipes_dict_list.append(recipe.to_dict())

    return jsonify(recipes_dict_list)


@app.route('/recipe', methods=['GET'])
def get_recipe_by_name():
    name = request.args.get('name')
    if name:
        recipe = recipe_service.get_recipe_by_name(name)
        if recipe:
            return jsonify(
                {'name': recipe.name,
                 'ingredients': recipe.ingredients}
                ), 200
        return jsonify({'error': 'recipe not founc!'}), 404
    return jsonify({'error': '"name" parameter is required!'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
    # app.run(debug=1)

import os
from flask import Flask, jsonify, request
from flask_cors import CORS # import CORS
from services import RecipeService

app = Flask(__name__)
# frontend specific URL
CORS(app, origins=['https://no-waste-frontend.onrender.com'])
# Allow all origins in development
# CORS(app, resources={r"/*": {"origins": "*"}})  
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
def get_recipes_by_name():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'name parameter is required!'}), 400

    recipes = recipe_service.find_recipes_by_partial_name(name)
    if recipes:
        recipes_list = [recipe.to_dict() for recipe in recipes]  # Ensure we serialize each recipe
        return jsonify(recipes_list), 200
    else:
        return jsonify({'error': 'No recipes found!'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
    # app.run(debug=1)

#!recipeenv/bin/python3
from flask import Flask, jsonify
import model

app = Flask(__name__)

DB = 'recipes.db'

@app.route('/recipe_bot/api/<int:recipe_id>', methods=['GET'])
def get_recipe():
    with model.Database(DB) as rdb:
        result = rdb.select_recipe(recipe_id)
        recipe = model.Recipe(result[0], result[1], result[2], result[3], result[4])
    return jsonify(recipe.dictionary)


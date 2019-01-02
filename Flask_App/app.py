#!recipeenv/bin/python3
from flask import Flask, jsonify
import model

app = Flask(__name__)

DB = 'recipes.db'

@app.route('/recipe_bot/api/get_all', methods=['GET'])
def all_recipes():
    with model.Database(DB) as rdb:
        
        return jsonify(recipe.__str__())
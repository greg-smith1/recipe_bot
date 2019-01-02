#!recipeenv/bin/python3
from flask import Flask
from model import Database, Recipe

app = Flask(__name__)

@app.route('/get_all')
def all_recipes():
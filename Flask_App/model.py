import sqlite3

class Database:

    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, trace):
        if not exc_type:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

def select_recipe(self, index):
    with Database as rdb:
        sql = """TODO SQL HERE"""
        rdb.cursor.execute(sql)
        result = rdb.cursor.fetchone()
        recipe = Recipe(result[0], result[1], result[2], result[3])
        return recipe

class Recipe:

    def __init__(self, title, cook_time, ingredients, steps=None, link=None):
        """Arguments:

        title - str, name of the recipe
        cook_time - int, cooking time in minutes, including preparation
        ingredients - dict, containing item:measurement pairs
        steps - list of strings, containing each step in the recipe
            default None, for easy one-pot/one-step recipes
        link - source of recipe if obtained online (None for original recipes)
        """
        self.title = title
        self.cook_time = cook_time
        self.ingredients = ingredients
        self.steps = steps
        self.link = link

    def print_steps(self):
        for i in range(len(self.steps)):
            print(i+1, self.steps[i])

    def __str__(self):
        print(self.title.title() + ':')
        for item, measurement in self.ingredients:
            print(item, measurement)


from model import Recipe

#TODO: Add testing logic here w/ asserts instead of name/main lines

if __name__=='__main__':
    steps = ['First step', 'Second step', 'Third step', 'And you\'re done!']
    ingredients = [('Carrots', '2 Cups'), ('Chocolate', '1tsp'), ('Mayonnaise', '1 Jar')]
    example = Recipe('Test Recipe', 35, ingredients, steps=steps)
    example.print_steps()
    example.__str__()


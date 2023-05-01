'''
Name: Justin Kachele
Assignment: PA 6
Due Date: May 1, 2023
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by professor and class syllabus.
'''
#Q1
def first_ingredient(f_name, recipeName):
    ingredient = "NOT FOUND"    # set it to this, will return if isn't changed
    recipies = open(f_name, 'r').readlines()    # open the file and read lines to list
    for i in range(len(recipies)):      # Loop through the recipies
        # read the recipe line to a list.
        # The first element if the name and the next elements are the ingredients
        recipe = recipies[i].strip()
        recipeList = recipe.split(',')
        # If the name matches the param, return the first ingredient (2nd element)
        if recipeList[0] == recipeName:
            ingredient = recipeList[1]
            break
    return ingredient


#Q2
def uses_this(inventory_file, recipe_file):
    # Open Files and read line as list
    inventoryInput = open(inventory_file, 'r').readlines()
    recipiesInput = open(recipe_file, 'r').readlines()

    # get list of ingredients from inventory
    ingredients = []
    for i in range(len(inventoryInput)):
        # Get the first element of the inventory line when split at the commas
        ingredients.append(inventoryInput[i].split(',')[0])

    # get list of recipes from recipiesInput
    recipies = []
    for i in range(len(recipiesInput)):
        recipies.append(recipiesInput[i].strip().split(','))

    # Loop through ingredients and find which recipe they are in
    ingredientRecipies = {}
    for ingredient in ingredients:
        recipiesList = []
        for recipe in recipies:
            for element in recipe:
                # if the ingredient in the recipe matches the ingredient were looking for,
                # add the recipe name to the list
                if element == ingredient:
                    recipiesList.append(recipe[0])
        ingredientRecipies[ingredient] = recipiesList
    return ingredientRecipies


#Q3
def in_stock(inventory_file, recipe_file, recipe_name):
    # Open Files and read line as list
    inventoryInput = open(inventory_file, 'r').readlines()
    recipiesInput = open(recipe_file, 'r').readlines()

    # loop through recipies
    recipeIngredients = []
    for recipe in recipiesInput:
        # read the recipe line to a list.
        # The first element if the name and the next elements are the ingredients
        recipeList = recipe.strip().split(',')
        # if the recipe matches parameter, remove first element and copy list
        if recipeList[0] == recipe_name:
            recipeList.pop(0)   # Remove the recipe name from the list
            recipeIngredients = recipeList
            break
    # If the loop finished without finding a match, return "NOT FOUND"
    else:
        return ["NOT FOUND"]

    ingredientList = []
    for line in inventoryInput:
        ingredientList.append(line.strip().split(','))
    
    # loop through all ingredients needed in the recipe
    # if the list of inventory contains it, add the ingredient and amount to the list
    # if ingredient is not in the inventory, add "NEED THIS" to the list
    ingredientStock = []
    for ingredient in recipeIngredients:
        for line in ingredientList:
            if line[0] == ingredient:
                stock = f"{ingredient}->{line[1]} {line[2]}"
                ingredientStock.append(stock)
                break
        else:
            stock = f"{ingredient}->NEED THIS"
            ingredientStock.append(stock)
    return ingredientStock


#Q4
def check_units(f_name, units = ['oz','each']):
    try:
        # Open Files and read line as list. Will through FileNotFoundError if incorrect name
        inventoryInput = open(f_name, 'r').readlines()

        # loop through inventory and split the line intp a list
        for line in inventoryInput:
            item = line.strip().split(',')
            # the unit is the 3rd element in the list, if missing, will through an index error
            itemUnit = item[2]
            for unit in units:
                if itemUnit == unit:
                    break
            # if the unit isnt in the units list
            else:
                return "incorrect units"

        return "all fine"
    except FileNotFoundError:
        return "inventory name incorrect"
    except IndexError:
        return "missing units"


#Q5
def first_five_ingr(f_name, recipeName):
    try:
        # Open Files and read line as list
        recipeInput = open(f_name, 'r').readlines()

        # loop through recipes and split each line into list
        for line in recipeInput:
            recipe = line.strip().split(',')
            # if the recipe name matches, return tuple with 5 ingredients
            # will through IndexError if not enough ingredients
            if recipe[0] == recipeName:
                return (recipe[1], recipe[2], recipe[3], recipe[4], recipe[5])
        return "recipe not found"
    except IndexError:
        return "not enough ingredients"


# print(first_ingredient("ingredients.csv", "pizza dough"))

# uses_this("inventory.csv", "ingredients.csv")
# print(uses_this("inventory.csv", "ingredients.csv"))

# print(in_stock("inventory.csv", "ingredients.csv", "quesadilla"))

# print(check_units('inventory.csv', ['pounds','oz']))
# print(check_units('inventory.csv'))
# print(check_units('inventoryA.csv', ['pounds','oz']))
# print(check_units('inventoryx.csv'))

# print(first_five_ingr('ingredients.csv', 'chili'))
# print(first_five_ingr('ingredients.csv', 'smoothie'))
# print(first_five_ingr('ingredients.csv', 'biryani'))

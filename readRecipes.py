import pandas as pd
import numpy as np
traindf = pd.read_json("train.json")
cuisineSet = set();
for cuisine in traindf['cuisine']:
    cuisineSet.add(cuisine)


ingredientSet = set();
for recipe in traindf['ingredients']:
    for ingredient in recipe:
        ingredientSet.add(ingredient)
print "There are %d recipes, %d types of cuisines and %d types of ingredients." % (traindf.__len__(), cuisine.__len__(), ingredientSet.__len__())


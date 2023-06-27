#%%
from itertools import permutations
import re
import numpy as np

def read_ingredients(file_path, exclude_calories = True):
    with open(file_path) as f:
        if exclude_calories:
            ingredients = [re.sub(', calories [-]?[\d]+', '', line.strip()) for line in f.readlines()]
        else:
            ingredients = [line.strip() for line in f.readlines()]

    properties = np.array([(re.findall("[-]?[\d]+", ingredient)) for ingredient in ingredients])
    properties = properties.astype(int)

    return properties


def valid_recipes(ingredient_count):
    recipes = permutations(range(101), ingredient_count)
    recipes = np.array([recipe for recipe in recipes if sum(recipe) == 100])

    return recipes


def main(calorie_count = None):
    if calorie_count == None:
        ingredients = read_ingredients('input.txt')
        recipes = valid_recipes(ingredients.shape[0])

        scores = np.dot(recipes,ingredients)
        scores[scores<0] = 0

        return scores.prod(axis=1).max()
    
    else:
        ingredients = read_ingredients('input.txt', exclude_calories = False)
        recipes = valid_recipes(ingredients.shape[0])
        scores = np.dot(recipes,ingredients)

        scores = scores[(scores[:,-1]== calorie_count),:-1]
        scores[scores<0] = 0

        return scores.prod(axis=1).max()



if __name__ == '__main__':
    part1 = main()
    part2 = main(500)


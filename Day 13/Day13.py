#%%
import re
import numpy as np
from itertools import permutations
from itertools import pairwise


with open('input.txt','r') as f:
    input = f.readlines()

neighbors = np.array([re.findall('[A-Z][a-z]+',line) for line in input])
people = np.unique(neighbors.reshape(-1))
#include this for part2
#people = np.append(people,"Me")

scores = np.array([re.findall('[a-z]+ [0-9]+',line)[0] for line in input])
scores = np.char.replace(scores, "lose ", "-")
scores = np.char.replace(scores, "gain ", "")

preferences = np.c_[neighbors,scores]

seating_arrangements = np.array([*permutations(people)])
seating_arrangements = np.c_[seating_arrangements[:,-1],seating_arrangements]

rankings = []
for arrangement in seating_arrangements:
    pairs = np.r_[
        np.array([*pairwise(arrangement)]),
        np.array([*pairwise(arrangement[::-1])])
        ]
    rank = sum([int(preferences[np.where((preferences[:,:2] == pair).all(1))[0][0],-1]) if (pair == preferences[:,:2]).all(1).any() else 0 for pair in pairs])
    rankings.append(rank)

max(rankings)
# %%

import re
from itertools import permutations
from itertools import pairwise

def optimal_seating_score(seating_file, include_me = False):
    
    with open(seating_file,'r') as f:
        input = f.readlines()

    #parse guests and their preferences from the input file
    neighbors = [re.findall('[A-Z][a-z]+',line) for line in input]
    scores= [(int(re.findall('[a-z]+ [0-9]+',line)[0].replace('lose ', '-').replace('gain ', '')))
     for line in input]
    people = set([pair[0] for pair in neighbors]) #unique guest names

    if include_me:
        people.add('Me')

    #Constructs nested hash table shell for people pairs and their happiness scores
    preferences = dict.fromkeys(people,0)
    for person in preferences.keys():
        preferences[person] = {name:0 for name in preferences.keys() if name !=person}
    
    #Adds the scores to the hash table
    for pair, score in zip(neighbors,scores):
        preferences[pair[0]][pair[1]] = score
    
    #constructs a list of all possible seating arrangments
    #repeats first value at the end to simulate circular table
    seating_arrangements = [permutation + (permutation[0],)
        for permutation in [*permutations(people)]]

    #Score each seating arrangement
    seating_scores = []
    for arrangement in seating_arrangements:
        #reverse arrangment append to the end to cover perspective of all guests
        pairs = list(pairwise(arrangement + arrangement[::-1][1:]))
        #look up happiness score for each pair and sum all scores
        score = sum([preferences[left][right] for left, right in pairs])
        seating_scores.append(score)

    return max(seating_scores)

part1 = optimal_seating_score('input.txt')
part2 = optimal_seating_score('input.txt', include_me=True)

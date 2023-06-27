#%%

import re
import numpy as np
with open('instructions.txt', 'r') as f:
    instructions = f.readlines()

coordinates = np.array([re.findall((r'\b\d+\b'), step) for step in instructions]).astype(int)
coordinates[:,-2:] =coordinates[:,-2:] + 1
lights = np.zeros((1000,1000))

for coord, instruction  in zip(coordinates, instructions):

    if instruction.startswith('turn on'):
        lights[coord[0]:coord[2],coord[1]:coord[3]] = 1
    elif instruction.startswith('turn off'):
        lights[coord[0]:coord[2],coord[1]:coord[3]] = 0
    else:
        lights[coord[0]:coord[2],coord[1]:coord[3]] = 1 - lights[coord[0]:coord[2],coord[1]:coord[3]]

lights.sum()

# %%
#part2
lights = np.zeros((1000,1000))

for coord, instruction  in zip(coordinates, instructions):

    if instruction.startswith('turn on'):
        lights[coord[0]:coord[2],coord[1]:coord[3]] += 1 
    elif instruction.startswith('turn off'):
        lights[coord[0]:coord[2],coord[1]:coord[3]] -= 1
        lights[lights < 0] = 0
    else:
        lights[coord[0]:coord[2],coord[1]:coord[3]] += 2

lights.sum()
# %%

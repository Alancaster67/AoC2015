#%%
import numpy as np

with open('Directions.txt','r') as f:
    directions = f.read()

#Convert instructions to mathematical vectors and pre-append the origin
directions = ('[0,0];' + directions) \
    .replace('^','[0,1];') \
    .replace('>','[1,0];') \
    .replace('v','[0,-1];') \
    .replace('<','[-1,0];')[:-1]

# Convert string to a 2-D array of directions
directions = np.array(list(map(eval, directions.split(';'))))

#Cumsum along the directions rows to get a list of coordinates
coordinates = np.cumsum(directions, axis=0)

#The count of unique coordinates is the answer to part1
unique_houses = np.unique(coordinates,axis=0).shape[0]

###Starting Part2

#Excluding the orign, assign EVEN indexed directions to santa
#Then pre-append origin to santa's directions
santa_direct = directions[1:][(np.arange(0,directions[1:].shape[0])%2) == 0]
santa_direct = np.append(np.array([[0,0]]), santa_direct, axis=0)

#Excluding the orign, assign ODD indexed directions to the robot
#Then pre-append origin to the robot's directions
robo_direct = directions[1:][(np.arange(0,directions[1:].shape[0])%2) == 1]
robo_direct = np.append(np.array([[0,0]]), robo_direct, axis=0)

#Append Santa's and Robot's coordinates together
combo_coords = np.append(np.cumsum(santa_direct, axis=0), np.cumsum(robo_direct, axis=0), axis=0)

#The count of unique coordinates in the combined array is the answer to part2
unique_houses_p2 = np.unique(combo_coords,axis=0).shape[0]
# %%

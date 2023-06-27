#%%
import numpy as np
from itertools import permutations

with open('Distances.txt','r') as f:
    distances = [dist.strip().split(' = ') for dist in f.readlines()]

distances = dict(
    distances + [
    [' '.join(flight.split()[::-1]), distance] for flight, distance in distances
    ])

locations = np.unique(
    np.array(
        [key.split(" to ") for key in dict(distances).keys()]
        )
    )

routes = np.array(list(permutations(locations)))
routes =np.char.add(
    np.char.add(routes[:,:-1]," to "),
     routes[:,1:])

total_distance = (np.vectorize(distances.get)(routes)
                .astype(int)
                .sum(axis=1))

print(
    f"""The answers to part1 and part2 are
    {total_distance.min()} and {total_distance.max()}, respectively"""
)

# %%

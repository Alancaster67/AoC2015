#%%
import numpy as np
with  open('input.txt','r') as f:
    instructions = np.array(list(f.read()))

decoder = np.vectorize({"(":1,")":-1}.get)
floors = decoder(instructions)

final_floor = floors[-1]
first_basement = np.where(np.cumsum(floors)==-1)[0][0] + 1
# %%

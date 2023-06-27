#%%
import numpy as np
with  open('input.txt','r') as f:
    instructions = f.read()

floors = np.vectorize({"(":1,")":-1}.get)(np.array(list(instructions)))

final_floor = floors[-1]
first_basement = np.where(np.cumsum(floors)==-1)[0][0] + 1
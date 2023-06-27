#%%
import pandas as pd

dims = pd.read_csv('boxes.txt', sep='x', names=['length','width','height'])

min_ribbon = (2*(dims.sum(axis=1) - dims.max(axis=1)) + dims.prod(axis=1)).sum()

dims['lw'] = dims['length']*dims['width']
dims['lh'] = dims['length']*dims['height']
dims['wh'] = dims['width']*dims['height']
dims['slack'] = dims.loc[:,['lw','lh','wh']].min(axis=1)
dims['min_area'] = (dims.iloc[:,3:-1]*2).sum(axis=1) + dims['slack']

min_paper = dims.min_area.sum()

# %%

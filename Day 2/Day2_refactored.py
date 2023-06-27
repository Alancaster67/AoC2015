#%%
import pandas as pd

dimensions = pd.read_csv('boxes.txt', sep='x', names=['length','width','height']).values
volumn = dimensions.prod(axis = 1)
area = (volumn[:,None]/dimensions).astype(int)

min_paper = ((area*2).sum(axis = 1) + area.min(axis =1)).sum()
min_ribbon = (2*(dimensions.sum(axis=1) - dimensions.max(axis=1)) + volumn).sum()
# %%

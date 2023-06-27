#%%
import hashlib
import numpy as np

with open('secret.txt','r') as f:
    secret = f.read()

keys = np.char.add(secret, np.arange(0,10000000).astype(str))
keys = np.char.encode(keys, encoding='utf-8')
keys = np.vectorize(lambda x: hashlib.md5(x).hexdigest())(keys)

part1_answer =np.where(np.char.startswith(keys,'00000'))[0][0]
part2_answer =np.where(np.char.startswith(keys,'000000'))[0][0]

# %%

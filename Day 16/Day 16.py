#%%
import re

with open('input.txt') as f:
    sues = [re.sub('Sue (\d)+: ','', sue.strip()) for sue in f.readlines()]

# %%
def check_sues(sues, part1=True):
    MFCSAM = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
    }

    count = 1
    for sue in sues:
        characteristics = re.findall('([a-z]+)', sue)
        vals = [int(score) for score in re.findall('([0-9]+)', sue)]

        if part1:

            if [MFCSAM[char] for char in characteristics] == vals:
                print(count)
            
            else:
                count += 1
        else:
            checks = []
            for char, val in zip(characteristics, vals):

                if char in ['cats', 'trees']:
                    checks.append(MFCSAM[char] < val)
                
                elif char in ['pomeranians', 'goldfish']:
                    checks.append(MFCSAM[char] > val)

                else:
                    checks.append(MFCSAM[char] == val)
            
            if all(checks):
                print(count)

            else:
                count+=1


# %%

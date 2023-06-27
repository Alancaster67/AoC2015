#%%
from itertools import combinations

def eggnog_storage(filepath = 'input.txt', part1=True):
    with open(filepath) as f:
        cups = [int(cup.strip()) for cup in f.readlines()]
    valid_combos = 0

    if part1:
        for cup_count in range(2,len(cups)+1):
            valid_combos += sum([sum(arangment) == 150 for arangment in combinations(cups, cup_count)])
        
        return(valid_combos)

    else:
        for cup_count in range(2,len(cups)+1):
            combos = [sum(arangment) == 150 for arangment in combinations(cups, cup_count)]

            if any(combos) and valid_combos == 0:
                return(sum(combos))


if __name__ == '__main__':
    print(eggnog_storage())
    print(eggnog_storage(part1=False))

# %%

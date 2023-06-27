#%%
from math import sqrt
from multiprocessing import cpu_count
import concurrent.futures
import time

def gifts_delivered(house:int) -> int:
    """Returns the number of gifts delivered to an input"""
    elf = 1
    gifts = set()
    while elf <= sqrt(house):
        if house % elf == 0:
            gifts.update([elf * 10, house / elf * 10 ])
        elf += 1
    return sum(gifts)

def lowest_house(target_gifts: int, min_house: int, max_house: int):
    houses = range(min_house,max_house)
    
    for house in houses:
        gifts = gifts_delivered(house)
        if gifts == target_gifts:
            return house
        
    return None
        

def divy_up_inputs(target_gifts, cpu_cores):
    even_distro = target_gifts//cpu_cores

    inputs= [
        (((elm)*even_distro)+1, ((elm+1)*even_distro)+1)
        for elm in range(0,cpu_cores)
        ]
    
    if target_gifts%cpu_cores !=0:
        inputs.append((inputs[-1][-1], target_gifts+1))
    
    return inputs


def main(target):

    inputs = divy_up_inputs(target, cpu_count())

    with concurrent.futures.ProcessPoolExecutor() as executor:
        processes = [executor.submit(lowest_house, (target, low, high)) for low,high in inputs]

        results = [proc.results for proc in processes]

    return results

# %%

if __name__ == '__main__':
    main(33100000)

# %%

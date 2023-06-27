#%%
with open('Santas_List.txt', 'r') as f:
    list = f.readlines()

code_count = sum([len(line.strip()) for line in list])
mem_count = sum([len(eval(line.strip())) for line in list])

part1 = code_count - mem_count

sum(2+ s.count("\\")+s.count('"') for s in list)


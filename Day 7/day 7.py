#%%
import numpy as np
with open('instructions.txt','r') as f:
    instructions = f.readlines()

py_instructions = np.array([(line.split(' -> ')[1] + ' = ' + line.split(' -> ')[0]).replace('\n','') for line in instructions])
translations = [
    ('AND','&'),
    ('OR','|'),
    ('NOT','~'),
    ('LSHIFT','<<'),
    ('RSHIFT','>>'),
    ('is', 'isa'),
    ('if','ifa'),
    ('in','ina'),
    ('as','asa')
    ]

for bit_op,py_op in translations:
    py_instructions = [line.replace(bit_op,py_op) for line in py_instructions]

#%%
#part 1 Do no run this cell before part 2
fail_count = 1
success_count = 0
while success_count != len(py_instructions):
    success_count = len(py_instructions)
    fail_count = 0
    for line in py_instructions:
        try:
            exec(line)
        except NameError:
            fail_count += 1
            pass
    success_count = success_count - fail_count

fail_count = 1
success_count = 0
# %%
#part 2 YOu must reset the kernal before running part 2 if part one cell was already run
py_instructions[np.where(np.char.startswith(py_instructions,'b = '))[0][0]] = 'b = 16076' 

fail_count = 1
success_count = 0
while success_count != len(py_instructions):
    success_count = len(py_instructions)
    fail_count = 0
    for line in py_instructions:
        try:
            exec(line)
        except NameError:
            fail_count += 1
            pass
    success_count = success_count - fail_count
# %%

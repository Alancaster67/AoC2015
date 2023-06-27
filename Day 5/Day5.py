#%%
#part1
import re
with open('words.txt', 'r') as f:
    words=f.readlines()

vowel_check = [len(re.findall('a|e|i|o|u', word)) >=3 for word in words]
double_check = [len(re.findall(r'(.)\1', word)) !=0 for word in words]
combo_check = [len(re.findall('ab|cd|pq|xy', word)) ==0 for word in words]

p1_nice_count = sum([all(check) for check in zip(vowel_check, double_check, combo_check)])
# %%
#part 2

double_pair_check = [len(re.findall(r'(\w{2}).*?(\1)', word)) !=0 for word in words]
split_pair_check = [len(re.findall(r'(.)(.)\1', word)) !=0 for word in words]

sum([all(check) for check in zip(double_pair_check, split_pair_check)])
# %%

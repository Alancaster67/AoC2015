import re
valid_char = list('abcdefghjkmnpqrstuvwxyz')
consecutive3 = [''.join(valid_char[ind-2:ind+1]) for ind in range(2,len(valid_char))]

def increment(password):

    #excludes 'l', 'i', and 'o'

    try:
        trailing_zs = len(re.match('z+',password[::-1])[0])
    except TypeError:
        trailing_zs = 0

    if len(password) == trailing_zs:
        return('a'*(len(password)+1))
    else:
        new_letter = valid_char[valid_char.index(password[-trailing_zs-1])+1]
        return(password[:-trailing_zs-1] + new_letter + 'a'*trailing_zs)


def is_valid(password):
    has_con3 = any((phrase in password) for phrase in consecutive3)
    no_invalids = all([char not in password for char in ['i', 'l', 'o']])
    has_doubles = len(re.findall(r'(.)\1', password)) >= 2
    
    return(all([has_con3, no_invalids, has_doubles]))

def new_password(password):
    valid = False
    while valid is False:
        password = increment(password)
        valid = is_valid(password)
    return(password)


with open('starting_password.txt','r') as f:
    password = f.read()

part1_password = new_password(password)
part2_password = new_password(part1_password)

print(f"Santa's first and second new passwords are {part1_password} and {part2_password} respectively")


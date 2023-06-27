#%%
import re

def parse_input(filepath = 'input.txt', reverse = False):
    with open(filepath) as f:
        input = f.readlines()

    if not reverse:
        replacements = [tuple(line.strip().split(' => ')) for line in input[:-2]]
    else:
        replacements = [tuple(line.strip().split(' => '))[::-1] for line in input[:-2]]
    
    med = input[-1].strip()

    return replacements, med

def rank_replacements(replacements):
    ranked=[(elm1, elm2, (len(elm1)-len(elm2))) for elm1, elm2 in replacements]
    ranked.sort(key = lambda x: x[-1], reverse=True)

    return ranked

def find_longest_replacements(ranked_replacements, med):
    
    for to_replace, replace_with, rep_length in ranked_replacements:
        replacement_length = 0
        if to_replace in med:
            replacement_length = rep_length
            break
        
    longest_replacements = [
        (to_replace, replace_with)
        for to_replace, replace_with, rep_length
        in ranked_replacements
        if rep_length == replacement_length]

    if len(longest_replacements) == 0 :
        raise ValueError("No valid replacements found")

    return longest_replacements


def find_replacement_index(to_replace:str, med:str|tuple):
    if isinstance(med, tuple):
        med=med[0]

    replacement_slices = [
        tuple([match.start(), match.start()+ len(to_replace)])
        for match in re.finditer(to_replace, med)]
    return replacement_slices


def make_replacement(start:int, end:int, replace_with:str, med:str) ->str|tuple:
    
    """if isinstance(med,tuple):
        new_med = (med[0][:start] + replace_with + med[0][end:], med[-1]+1)

    else:
        new_med = med[:start] + replace_with + med[end:]"""

    new_med = med[:start] + replace_with + med[end:]
    return new_med

def calibrate(replacements,med):

    possible_meds = []
    for to_replace, replace_with in replacements:
        
        slices = find_replacement_index(to_replace=to_replace, med=med)

        for start, end in slices:
            
            new_med = make_replacement(
                start=start,
                end=end,
                replace_with=replace_with,
                med=med
                )
            
            possible_meds.append(new_med)
    
    return possible_meds

def my_part2_attempt():
    """This is my attempt to get answer to the second part but
    the code takes too long to run."""
    replacements, target_med = parse_input('input_part2.txt')
    ranked_reps = rank_replacements(replacements=replacements)

    created_meds = set([target_med])
    count = 0
    while 'e' not in created_meds:
        

        new_meds = set()
        for m in created_meds:
            best_reps = find_longest_replacements(ranked_reps, m)
            replaced_meds = calibrate(replacements=best_reps, med=m)

            new_meds.update(replaced_meds)
        
        created_meds = new_meds
        count += 1
    
    return count

def part2_with_help():
    """
    The answer is reached by subtracting out the number of atoms
    that need 2 replacements (Ar and Y) from the total number of atoms
    in the target molecule. The subtraction of 1 is just to go from an
    atom to an electron.
    This calculation was explained by salt-die on the Python Discord.
    """
    replacements, target_med = parse_input('input_part2.txt')

    answer = (len(re.findall(r"[A-Z][a-z]*", target_med))
    - 2 * len(re.findall("Y", target_med))
    -2 * len(re.findall("Ar", target_med))
    -1)
    return answer

#%%

if __name__ == '__main__':
    replacements, med = parse_input()
    part1= len(set(calibrate(replacements=replacements, med=med)))
    part2 = part2_with_help()
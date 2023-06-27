from itertools import groupby

def look_and_say(start: str, iterations: int) -> int:
    digits = [start]
    count = 0
    while count<iterations:
        #As strings, add length of the group and key of the groupby for the last element in digist
        converted_str = ''.join([str(len(list(group))) + key for key, group in groupby(list(digits[-1]))])
        digits.append(converted_str)
        count+=1

    return len(digits[-1])



with open('input.txt', 'r') as f:
    start = f.read()

print(
    f"""
    part 1 answer = {look_and_say(start, 40)}
    part 2 answer = {look_and_say(start, 50)}
    """)

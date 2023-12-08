from utils import readfile
import numpy as np
import re

# read data
data = readfile(r"2023/day8.txt")
regex = re.compile('([0-9A-Z]{3})')

direction=data[0]

maps = [regex.findall(line) for line in data[2:]]
d = {line[0]:(line[1], line[2]) for line in maps}

key = 'AAA'
counter = 0
while key != 'ZZZ':
    key = d[key][0 if direction[counter%len(direction)] == 'L' else 1]
    counter+=1

print("Problem 1: ", counter)


# get all key finishing by A
starting_keys = [key for key in d.keys() if key[2] == 'A']
max_=len(starting_keys)

results = {}
counters = {}
for key in starting_keys:
    results[key] = []
    counter = 0
    dir = 0 if direction[counter%len(direction)] == 'L' else 1
    k = d[key][dir]

    while True:
        if results[key] != []:
            if k in np.array(results[key]).T[0] and str(dir) in np.array(results[key]).T[1]:
                break

        counter += 1
        if k[2] == 'Z':
            results[key].append([k, dir, counter])
        dir = 0 if direction[counter%len(direction)] == 'L' else 1
        k = d[k][0 if direction[counter%len(direction)] == 'L' else 1]


res = np.array(list(results.values())).T[2][0].astype(int)


def get_result(array):
    if len(array) == 2:
        lcm = np.lcm(array[0], array[1])
        return lcm if lcm >= 0 else lcm + 2**32
    else:
        return get_result(np.concatenate([[get_result(array[:2])], array[2:]]))










while sum([1 if key[2] == 'Z' else 0 for key in keys ]) != max_:
    dir = 0 if direction[counter%len(direction)] == 'L' else 1
    keys = [
        d[key][dir]
        for key in keys
    ]
    counter += 1
    # print(keys)

print("Problem 2: ", counter)
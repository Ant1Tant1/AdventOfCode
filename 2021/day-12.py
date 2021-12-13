from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-12.txt", my_type=str)

# data = [
#     "start-A",
#     "start-b",
#     "A-c",
#     "A-b",
#     "b-d",
#     "A-end",
#     "b-end"
# ]

# data = [
# "dc-end",
# "HN-start",
# "start-kj",
# "dc-start",
# "dc-HN",
# "LN-dc",
# "HN-end",
# "kj-sa",
# "kj-HN",
# "kj-dc",
# ]

# data = [
# "fs-end",
# "he-DX",
# "fs-he",
# "start-DX",
# "pj-DX",
# "end-zg",
# "zg-sl",
# "zg-pj",
# "pj-he",
# "RW-he",
# "fs-DX",
# "pj-RW",
# "zg-RW",
# "start-pj",
# "he-WI",
# "zg-he",
# "pj-fs",
# "start-RW"
# ]

d = {}
for line in data:
    key, value = line.split('-')
    if key not in d.keys():
        d[key] = []
    d[key].append(value)
    if value not in d.keys():
        d[value] = []
    d[value].append(key)

# ===========  PB 1 & 2  ===========
# need to find path going from start to end
# passing only once in lower case values

def get_next_possible_values_2(key, v_places):
    res = []
    for val in d[key]:
        if (val == 'start'): # | (v_places[val] >= 1): # PB 1
            continue        
        
        # PB 2
        if (max(v_places.values()) >= 2) & (v_places[val] >= 1):
            continue

        res.append(val)
    return res



def f_2(key, visited_places, path, results):
    path.append(key)
    
    if key == "end":
        results += 1
        # print(path)
        return results

    if key.islower(): 
        visited_places[key] += 1

    next_val = get_next_possible_values_2(key, dict(visited_places))

    # recursive loop
    for v in next_val:
        results = f_2(v, dict(visited_places), list(path), results)

    return results

visited_places = {key:0 for key in d.keys()}
f_2('start', visited_places, [], 0)
from utils import readfile
import numpy as np
from collections import Counter

# read data
data = readfile(r"2021/day-14.txt", my_type=str)

# data = [
#     "NNCB",
#     "",
#     "CH -> B",
#     "HH -> N",
#     "CB -> H",
#     "NH -> C",
#     "HB -> C",
#     "HC -> B",
#     "HN -> C",
#     "NN -> C",
#     "BH -> H",
#     "NC -> B",
#     "NB -> B",
#     "BN -> B",
#     "BB -> N",
#     "BC -> B",
#     "CC -> N",
#     "CN -> C"
# ]

# read data
polymer = data[0]

transformationDic = {line.split(' -> ')[0]:line.split(' -> ')[1] for line in data[2:]}

# ===========  PB 1 - LAME SOLUTION ===========
def get_new_polymer(p):
    n = len(p)
    new_letters = [transformationDic[p[i:i+2]] for i in range(n-1)]
    new_p =  "".join([ p[i] + new_letters[i] for i in range(n-1)])
    new_p += p[n-1]
    return new_p

for i in range(10):
    polymer = get_new_polymer(polymer)

polymer_10 = polymer
res = Counter(polymer_10)
most_common = res.most_common()
print(most_common[0][1] - most_common[-1][1])


# ===========  PB 1 & 2 - BETTER OPTION FOR SMALL AND LARGE COMPUTATIONS ===========
polymer = data[0]

pairs = { key: 0 for key in transformationDic.keys()}
for i in range(len(polymer) -1):
    pairs[polymer[i:i+2]] += 1

def next_turn(p):
    new_pairs = {k:0 for k in p.keys()}
    for key, val in p.items():
        if val == 0:
            continue
        
        l1, l2 = key[0] + transformationDic[key], transformationDic[key] + key[1]
        new_pairs[l1] += val
        new_pairs[l2] += val

    return new_pairs

# compute with a dict
p = pairs.copy()
for i in range(40):
    p = next_turn(p)

# get the number of elements for each base
res = {}
for key, val in p.items():
    for char in [key[0], key[1]]:
        if char in res.keys():
            res[char] += val
        else:
            res[char] = val

most_common = Counter(res).most_common()
print(np.ceil((most_common[0][1] - most_common[-1][1])/ 2))




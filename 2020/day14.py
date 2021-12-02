from numpy.core.fromnumeric import reshape
from utils import readfile
import numpy as np
import itertools

data = readfile("2020/day14.txt")
# ======================= PB 1 ===================
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def extract_data(line):
    key, value = line.split(" = ")
    if key != "mask":
        key = key.replace("mem[", "")
        key = key.replace("]", "")
        value = int(value)
    return key, value

def apply_mask(value):
    val = format(value, "036b")
    res = np.zeros(36, dtype=str)
    for i, (j, k) in enumerate(zip(val, mask)):      
        if k == 'X' or "":
            res[i] = j
        else:
            res[i] = k 
    
    res = "".join(res)
    return int(res, 2)

results = {}
for d in data:
    key, value = extract_data(d)
    if key == 'mask':
        mask = value
    else:
        results[key] = apply_mask(value)

print('Pb 1:', np.sum(list(results.values())))


# ================ PB 2 =====================
def get_keys(key):
    val = format(key, "036b")
    res = np.zeros(36, dtype=str)
    nb_X = 0
    idx_X = []
    for i, (j, k) in enumerate(zip(val, mask)):   
        if k == '0':
            res[i] = j
        elif k == 'X':
            res[i] = k
            nb_X += 1
            idx_X.append(i)
        else:
            res[i] = k
    
    combinations = list(itertools.product(*[['0','1']] * nb_X))

    keys = np.zeros((len(combinations), 36), dtype=str)
    for i in range(len(combinations)):
        keys[i] = res
    for i, tup in enumerate(combinations):
        for (tup_value, index) in zip(tup, idx_X):
            keys[i][index] = tup_value

    # convert back to str (after casting int)
    keykeys = [str(int("".join(key), 2)) for key in keys]


    return keykeys
    return int(res, 2)

results = {}
for d in data:
    key, value = extract_data(d)
    if key == 'mask':
        mask = value
    else:
        for k in get_keys(int(key)):
            results[k] = float(value)

print("Pb 2:", np.sum(list(results.values())))
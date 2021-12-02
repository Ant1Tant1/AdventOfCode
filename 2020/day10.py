from os import read

from numpy.core.defchararray import multiply
from numpy.core.fromnumeric import prod, product
from utils import readfile
import numpy as np
import itertools
data = readfile("2020/day10.txt", my_type=int)
data1 = readfile("2020/day10-1.txt", my_type=int)

# ============================ PB 1 =============================================
def use_adapters(data):
    # sort data
    data.sort()
    # create an array containing data + 0 at first pos and last value + 3 at the last pos
    dt = np.zeros(len(data)+2)
    dt[1:-1] = data
    dt[-1] = dt[-2] + 3
    # get diff
    return np.diff(dt)

diff = use_adapters(data)
a, b = (diff == 1).sum(), (diff == 3).sum()
print(f"Pb 1:\nNumer of diff = 1: {a}\nNumber of diff = 2: {b}\nPb 1: {a*b}")

# ================================ PB 2 =========================================
def nb_of_combinations(n, threshold=3):
    # get number of possible combination of n one following each other
    # given a threshold max between two following numbers
    
    # cast int
    n = int(n)

    # create a list of binary combination
    # I use n-1 because the last number will have to be true anyways (jump of 3)
    boolean_combinations = list(itertools.product(*[[False,True]] * (n-1)))
    nb_combinations = 0
    my_range = np.arange(n+1)
    for b in boolean_combinations:
        concat_list = [True] + list(b) + [True]
        if len(np.where(np.diff(my_range[concat_list]) > threshold)[0]) == 0:
            nb_combinations += 1
    return nb_combinations

# add a 0 to diff
dff = np.zeros(len(diff)+1)
dff[1:] = diff

# get where diff == 3 -> these number cannot be changed
where_diff_3 = np.where(dff == 3)[0]

# add a 0 to where_diff_3
index_diff_3 = np.zeros(len(where_diff_3)+1)
index_diff_3[1:] = where_diff_3

# get the number of consecutive 1 (you add to substract 1 to get it)
diff_diff_3 = np.diff(index_diff_3) - 1

n_comb = float(1)
for i, n in enumerate(diff_diff_3):
    # handle case of following 3
    if n == 0:
        print("Number of combination {:2}: {}".format(i, 1))
        continue
    # get number of combinations
    res = nb_of_combinations(n)
    n_comb *= res
    print("Number of combination {:2}: {}".format(i, res))


print("Pb 2: ", n_comb)
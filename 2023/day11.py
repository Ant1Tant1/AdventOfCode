from utils import readfile
import numpy as np
import re

# read data
data = readfile(r"2023/day11.txt")
data = np.array([[
        c for c in line
    ]
    for line in data
])

x, y = np.where(data == "#")
r = set(range(len(data)))
row_to_duplicate = r.difference(set(x))
col_to_duplicate = r.difference(set(y))

for i in sorted(row_to_duplicate, reverse=True):
    data = np.insert(data, i, '.', axis=0)

for j in sorted(col_to_duplicate, reverse=True):
    data = np.insert(data, j, '.', axis=1)

x, y = np.where(data == "#")

import math
res = np.zeros(
    math.comb(len(x), 2)
)

idx=0
for i in range(len(x)-1):
    for j in range(i+1, len(x)):
        res[idx] = np.abs(x[j]-x[i])+np.abs(y[j]-y[i])
        idx+=1

print("Problem 1: ", res.sum())


data = readfile(r"2023/day11.txt")
data = np.array([[
        c for c in line
    ]
    for line in data
])

x, y = np.where(data == "#")
r = set(range(len(data)))
row_to_duplicate = r.difference(set(x))
col_to_duplicate = r.difference(set(y))


idx=0
expansion = 1000000
res = np.zeros(math.comb(len(x), 2))
for i in range(len(x)-1):
    for j in range(i+1, len(x)):
        # x will always be in the right order
        res[idx] += (
                x[j] - x[i]
                + len(set(np.arange(x[i], x[j])).intersection(row_to_duplicate))*(expansion-1) \
            )
        res[idx] += (
                y[j] - y[i]
                + len(set(np.arange(y[i], y[j])).intersection(col_to_duplicate))*(expansion-1)
            ) if y[j] >= y[i] else (
                y[i]-y[j]
                + len(set(np.arange(y[j], y[i])).intersection(col_to_duplicate))*(expansion-1)
            )
        idx+=1

print("Problem 2: ", res.sum())
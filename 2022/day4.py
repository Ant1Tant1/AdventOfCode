from utils import readfile
import numpy as np

# read data
data = readfile(r"day4.txt")

res = 0
for line in data:
    p1, p2 = line.split(',')
    p1_min, p1_max = [float(x) for x in p1.split('-')]
    p2_min, p2_max = [float(x) for x in p2.split('-')]

    if (p1_min >= p2_min) & (p1_max <= p2_max) \
    | (p1_min <= p2_min) & (p1_max >= p2_max):
        res += 1

print("first problem: ", res)

res = 0
for line in data:
    p1, p2 = line.split(',')
    p1_min, p1_max = [float(x) for x in p1.split('-')]
    p2_min, p2_max = [float(x) for x in p2.split('-')]

    if (p1_min >= p2_min) & (p1_max <= p2_max) \
     | (p1_min <= p2_min) & (p1_max >= p2_max) \
     | (p1_min >= p2_min) & (p1_min <= p2_max) \
     | (p1_max >= p2_min) & (p1_max <= p2_max) \
     | (p2_min >= p1_min) & (p2_min <= p1_max) \
     | (p2_max >= p1_min) & (p2_max <= p1_max):
        res += 1

print("second problem: ", res)
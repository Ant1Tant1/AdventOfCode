from utils import readfile
import numpy as np

# read data
data = readfile(r"2022/day6.txt")
data = data[0]


for i in range(len(data)-4):
    if len(set(data[i:i+4])) == 4:
        break

print("first pb: ", i + 4)

n=14
for i in range(len(data)-n):
    buffer = data[i:i+n]
    if len(set(buffer)) == n:
        break

print("second pb: ", i + n)

from utils import readfile
import numpy as np

# read data
data = readfile(r"day6.txt")
data = data[0]


for i in range(len(data)-4):
    buffer = data[i:i+4]
    if len(set(buffer)) == 4:
        break

print("first pb: ", i + 4)

n=14
for i in range(len(data)-n):
    buffer = data[i:i+n]
    if len(set(buffer)) == n:
        break

print("second pb: ", i + n)

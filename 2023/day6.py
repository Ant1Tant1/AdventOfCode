from utils import readfile
import numpy as np
import re

# read data
data = readfile(r"2023/day6.txt")
regex = re.compile('[0-9]+')

time, dist = np.array([
    [int(i) for i in regex.findall(line)]
    for line in data
])

def equation(time, distance):
    delta = time**2 - 4*distance
    x1 = (time + np.sqrt(delta))/2
    x2 = (time - np.sqrt(delta))/2
    return np.ceil(x1-1) - np.floor(x2+1) + 1

print("Problem 1: ", equation(time, dist).prod())

time, dist = (
    int("".join(regex.findall(line)))
    for line in data
)

print("Problem 2: ", equation(time, dist))
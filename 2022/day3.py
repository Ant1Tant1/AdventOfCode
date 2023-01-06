from utils import readfile
import numpy as np

# read data
data = readfile(r"2022/day3.txt")


import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1

for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 27

res = []
for line in data:
    n = len(line)
    a, b = line[:n//2], line[n//2:]

    res.append(set(a).intersection(b).pop())

print("first solution: ", np.sum([values[letter] for letter in res]))


res = []
for i in range(len(data)//3):
    a = data[3*i]
    b = data[3*i+1]
    c = data[3*i+2]

    res.append(set(a).intersection(b).intersection(c).pop())

print("second solution: ", np.sum([values[letter] for letter in res]))

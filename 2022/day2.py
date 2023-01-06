from utils import readfile
import numpy as np

# read data
data = readfile(r"2022/day2.txt")

res = 0
for d in data:
    a, b = d.split(" ")
    
    if (a == "A") & (b == "Y") \
    | (a == "B") & (b == "Z") \
    | (a == "C") & (b == "X"):
        res += 6
    elif (a == "A") & (b == "X") \
    | (a == "B") & (b == "Y") \
    | (a == "C") & (b == "Z"):
        res += 3
    else:
        res += 0

    if b == "X":
        res += 1
    elif b == "Y":
        res += 2
    else:
        res += 3

print("first problem: ", res)

res = 0
for d in data:
    a, b = d.split(" ")

    if b == "X":
        if a == "A":
            res += 3
        elif a == "B":
            res += 1
        elif a == "C":
            res += 2
    
    if b == "Y":
        res += 3
        if a == "A":
            res += 1
        elif a == "B":
            res += 2
        elif a == "C":
            res += 3

    if b == "Z":
        res += 6
        if a == "A":
            res += 2
        elif a == "B":
            res += 3
        elif a == "C":
            res += 1

print("second problem: ", res)
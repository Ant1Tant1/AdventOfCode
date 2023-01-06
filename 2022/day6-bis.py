from utils import readfile
import numpy as np

# read data
data = readfile(r"2022/day6.txt")
data = data[0]

res = [len(set(data[i:i+4])) == 4 for i in range(len(data)-3)]

print("first solution: ", (np.argwhere(res)+4)[0])

def method(n):
    res = [len(set(data[i:i+n])) == n for i in range(len(data)-n+1)]
    return (np.argwhere(res)+n)[0]

print("first solution: ", method(4))
print("second solution: ", method(14))

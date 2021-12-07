from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-7.txt", my_type=str)

# data = ["16,1,2,0,4,2,7,1,2,14"]
data = np.array(data[0].split(','), dtype=int)

# pb 1
n = max(data)
val = [np.sum(np.abs(data - i)) for i in range(n)]
print(min(val))

# pb 2
val = [np.sum(np.abs(data - i) * (np.abs(data - i) + 1) / 2) for i in range(n)]
print(min(val))
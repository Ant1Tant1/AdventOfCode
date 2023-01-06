from utils import readfile
import numpy as np

# read data
data = readfile(r"2022/day1.txt")

res = []
r= 0
for d in data:
    if d == '':
        res.append(r)
        r = 0
    else:
        r += float(d)
res.append(r)

print("first answer: ", np.max(res))

final_answer = np.sum(np.sort(res)[-3:])

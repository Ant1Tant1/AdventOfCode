from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-5.txt", my_type=str)

# initialize vectors
x1 = np.zeros(len(data), dtype=int)
x2 = np.zeros(len(data), dtype=int)
y1 = np.zeros(len(data), dtype=int)
y2 = np.zeros(len(data), dtype=int)

# get data
for i, line in enumerate(data):
    splt = line.split(' -> ')
    x1[i], y1[i] = splt[0].split(',')
    x2[i], y2[i] = splt[1].split(',')
    
    

# -------- FIRST PB -------------------
n = np.max([x1, x2, y1, y2]) + 1
table = np.zeros((n,n))

def get_min_max(a, b):
    mn = min(a, b)
    mx = max(a,b)
    return mn, mx

c = (x1 == x2) | (y1 == y2)
for i, b in enumerate(c):
    if not b:
        continue
    if x1[i] == x2[i]:
        ymin, ymax = get_min_max(y1[i], y2[i])
        table[x1[i], ymin:ymax+1] += 1
    if y1[i] == y2[i]:
        xmin, xmax = get_min_max(x1[i], x2[i])
        table[xmin:xmax+1, y1[i]] += 1

res = (table >= 2).sum()
print(res)

# ---------- SECOND PB --------------
n = np.max([x1, x2, y1, y2]) + 1
table = np.zeros((n,n))

for i in range(len(x1)):
    if x1[i] == x2[i]:
        ymin, ymax = get_min_max(y1[i], y2[i])
        table[x1[i], ymin:ymax+1] += 1
    elif y1[i] == y2[i]:
        xmin, xmax = get_min_max(x1[i], x2[i])
        table[xmin:xmax+1, y1[i]] += 1
    elif x1[i] - x2[i] == y1[i] - y2[i]:
        xmin, xmax = get_min_max(x1[i], x2[i])
        ymin, ymax = get_min_max(y1[i], y2[i])
        diag = np.zeros((xmax+1-xmin, ymax+1-ymin))
        np.fill_diagonal(diag, 1)
        table[xmin:xmax+1, ymin:ymax+1] += diag
    elif x1[i] - x2[i] == -y1[i] + y2[i]:
        xmin, xmax = get_min_max(x1[i], x2[i])
        ymin, ymax = get_min_max(y1[i], y2[i])
        diag = np.zeros((xmax+1-xmin, ymax+1-ymin))
        np.fill_diagonal(diag, 1)
        diag = np.fliplr(diag)
        table[xmin:xmax+1, ymin:ymax+1] += diag
    else:
        print("error")

res = (table >= 2).sum()
print(res)
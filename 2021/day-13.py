from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-13.txt", my_type=str)

# data = [
#     "6,10",
#     "0,14",
#     "9,10",
#     "0,3",
#     "10,4",
#     "4,11",
#     "6,0",
#     "6,12",
#     "4,1",
#     "0,13",
#     "10,12",
#     "3,4",
#     "3,0",
#     "8,4",
#     "1,10",
#     "2,14",
#     "8,10",
#     "9,0",
#     "",
#     "fold along y=7",
#     "fold along x=5"
# ]

# get data
i = np.where(np.asarray(data) == "")[0][0]
d = np.array([data[j].split(',') for j in range(int(i))], dtype=int)
fold_instr = [(data[j].split('=')[0][-1],data[j].split('=')[1]) for j in range(int(i)+1, len(data))]


# ===========  PB 1 & 2  ===========
# get d size
m = max(d[:, 1]) + 1 
n = max(d[:, 0]) + 1
grid = np.zeros((m, n), dtype=int)

for (x, y) in d: grid[y, x]=True

def get_fold_instr(instr, grid):
    if instr[0]=='x':
        j = int(instr[1])
        g = np.zeros((m, j), dtype=bool)
        g = (grid[:, :j]) | np.fliplr(grid[:, j+1:])
    else:
        i = int(instr[1])
        g = np.zeros((i, n), dtype=bool)
        g = (grid[:i, :]) | np.flipud(grid[i+1:, :])
    return g

for instr in fold_instr:
    grid = get_fold_instr(instr, grid)

# print the characters
p,q = grid.shape
nb_char = 8
for i in range(nb_char):
    print('\n', grid[:, q//nb_char*i:q//nb_char*(i+1)])

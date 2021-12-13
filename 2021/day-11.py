from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-11.txt", my_type=str)

# data = [
# "5483143223",
# "2745854711",
# "5264556173",
# "6141336146",
# "6357385478",
# "4167524645",
# "2176841721",
# "6882881134",
# "4846848554",
# "5283751526"]

data = np.array([list(string) for string in data], dtype=int)

# ===========  PB 1 & 2  ===========
def get_condition(data, val=9):
    return np.where(data > val)

def increase_adj_val(dt, i, j, flash_nb):
    # set mask to true
    mask[i,j] = True
    # pad array to avoid limit cases
    d = np.pad(dt, 1, constant_values = -100)
    # take padding into consideration
    i += 1; j += 1 
    # 8 digit around i, j
    c = ([i-1, i-1, i-1, i, i, i+1, i+1, i+1], 
         [j-1, j, j+1, j-1, j+1, j-1, j, j+1])
    # add 1
    d[c] += 1
    # get dt back
    dt = d[1:-1, 1:-1]
    # Recursive part
    cond = get_condition(dt)
    if np.shape(cond) [1] != 0:
        for i1, j1 in zip(cond[0], cond[1]):
            if not mask[i1, j1]:
                dt, flash_nb = increase_adj_val(dt, i1, j1, flash_nb+1)
    return dt, flash_nb


dt = data.copy()
mask = np.zeros(dt.shape, dtype=bool)
flash_nb = 0
k = 0
while 1:
    k += 1
    mask = np.zeros(dt.shape, dtype=bool)
    dt += 1
    cond = get_condition(dt)
    if np.shape(cond) [1] != 0:
        for i, j in zip(cond[0], cond[1]):
            if not mask[i, j]:
                dt, flash_nb = increase_adj_val(dt, i, j, flash_nb+1) # first pb
    dt[get_condition(dt)] = 0
    # second problem
    if dt.sum() == 0:
        res = k
        break
    
print(dt, '\n\n', flash_nb, res)
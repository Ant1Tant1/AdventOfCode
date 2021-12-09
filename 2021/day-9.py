from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-9.txt", my_type=str)

# data = [
#     "2199943210",
#     "3987894921",
#     "9856789892",
#     "8767896789",
#     "9899965678"
# ]

data = np.array([list(string) for string in data], dtype=int)

# ===========  PB 1  ===========
def everything_unless_borders(ax):
    return (data - np.roll(data, 1, axis=ax) < 0) \
            & (data - np.roll(data, -1, axis=ax) < 0)

n, m = data.shape

# Handle general case
c = everything_unless_borders(1) & everything_unless_borders(0)

# handle borders
# first line
c[0, 1:m-1] = (data[0, 1:m-1] < data[1, 1:m-1]) & (data[0, 1:m-1] < data[0, 0:m-2]) & (data[0, 1:m-1] < data[0, 2:m])
c[n-1, 1:m-1] = (data[n-1, 1:m-1] < data[n-2, 1:m-1]) & (data[n-1, 1:m-1] < data[n-1, 0:m-2]) & (data[n-1, 1:m-1] < data[n-1, 2:m])
c[1:n-1, 0] = (data[1:n-1, 0] < data[1:n-1, 1]) & (data[1:n-1, 0] < data[0:n-2, 0]) & (data[1:n-1, 0] < data[2:n, 0])
c[1:n-1, m-1] = (data[1:n-1, m-1] < data[1:n-1, m-2]) & (data[1:n-1, m-1] < data[0:n-2, m-1]) & (data[1:n-1, m-1] < data[2:n, m-1])

c[0, 0] = (data[0,0] < data[0,1]) & (data[0,0] < data[1,0])
c[n-1, 0] = (data[n-1,0] < data[n-2,0]) & (data[n-1,0] < data[n-1,1])
c[n-1, m-1] = (data[n-1,m-1] < data[n-2,m-1]) & (data[n-1,0] < data[n-1,m-2])
c[0, m-1] = (data[0,m-1] < data[0,m-2]) & (data[0,m-1] < data[1,m-1])

print(sum(data[c]+1))


# ===========  PB 1  ===========
WALL = 9
def get_data(i, j, visited_places):
    val = 1
    visited_places.append((i,j))
    # print(i, j)
    if (i != n-1) and (data[i+1, j] != WALL) and ((i+1, j) not in visited_places):
        val += get_data(i+1, j, visited_places)
    if (i != 0) and (data[i-1, j] != WALL) and ((i-1, j) not in visited_places):
        val += get_data(i-1, j, visited_places)
    if (j != m-1) and (data[i, j+1] != WALL) and ((i, j+1) not in visited_places):
        val += get_data(i, j+1, visited_places)
    if (j != 0) and (data[i, j-1] != WALL) and ((i, j-1) not in visited_places):
        val += get_data(i, j-1, visited_places)
    return val


row_ind, col_ind = np.where(c)


res = []
for i, j in zip(row_ind, col_ind):
    visited_places = []
    val = get_data(i, j, visited_places)
    res.append(val)
    
results = np.asarray(sorted(res)[-3:])
print(results, results.prod())

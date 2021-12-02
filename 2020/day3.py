import numpy as np
from utils import readfile

# get data
data = readfile(r"2020/day3.txt")

# get nb lines and col
nb_lines = len(data)
nb_col = len(data[0])
print(f"The pb has {nb_lines} lines and {nb_col} columns")

# ================ RECURSIVE SOLUTION =====================
def recursive_sol(i=0, j=0, inc_i=1, inc_j=1, solution=0):
    # ensure next value exist or return solution
    if i + inc_i > nb_lines:
        return solution 

    # get actual solution
    if data[i][j] == '#':
        solution += 1

    # get next pos
    i+=inc_i
    j = (j+inc_j) % nb_col

    # get value for next pos
    return recursive_sol(i, j, inc_i, inc_j, solution)


    
print("solution pb 1: ", recursive_sol(inc_i=1, inc_j=3))

my_inc = np.array([[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]])
print("====== pb 2 =========")
tot_sol =1
for index, inc in enumerate(my_inc):
    sol = recursive_sol(inc_i=inc[0], inc_j=inc[1])
    tot_sol *= sol
    print("indiv sol: ", sol)
print("solution pb 2: ", tot_sol)


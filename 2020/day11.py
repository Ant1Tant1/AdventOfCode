from numpy.lib.function_base import vectorize
from utils import readfile
import numpy as np
d = readfile("2020/day11.txt")

def split(word): 
    return [char for char in word] 

d = np.array([split(dt) for dt in d])
nb_lines, nb_cols = d.shape

# ================== PB 1 ==============================

# return 0 if seat is empty (or not seat), 1 otherwise
def test_empty(data, i,j):
    if data[i][j] in ('L', '.'):
        return 0
    else:
        return 1

def test_neighbours(data, data_copy, i,j):
    # if i,j is a floor, go ahead
    if data[i][j] == '.':
        return 

    # create combinations of neighbours
    combinations = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

    # iterate through neighbours
    res = 0
    for iter_i, iter_j in combinations:
        # handle limit cases
        if i + iter_i < 0 or i + iter_i >= nb_lines or\
           j + iter_j < 0 or j + iter_j >= nb_cols:
            continue

        # handle floor
        res += test_empty(data, i + iter_i, j + iter_j)

    # get results
    if data[i][j] == "L" and res == 0:
        data_copy[i][j] = "#"
        return True

    if data[i][j] =='#' and res >= 4:
        data_copy[i][j] = "L"
        return True

    return False

def pb1(data):
    data_copy = np.copy(data)
    res = 1
    while res:
        res = 0
        for i in np.arange(nb_lines):
            for j in np.arange(nb_cols):
                if test_neighbours(data, data_copy, i,j):
                    res += 1
        data = np.copy(data_copy)
    return data

dt1 = pb1(np.copy(d))
print("Pb 1: ", len(np.where(dt1 == "#")[0]))

# ====================== PB 2 ==========================
# return 0 if seat is empty (or not seat), 1 otherwise
def test_empty_2(data, i,j):
    if data[i][j] == 'L':
        return 0
    elif data[i][j] == '#':
        return 1
    else:
        return -1

def test_neighbours_2(data, data_copy, i,j):
    # if i,j is a floor, go ahead
    if data[i][j] == '.':
        return 

    # create combinations of neighbours
    combinations = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

    # iterate through neighbours
    res = 0
    for iter_i, iter_j in combinations:
        # handle limit cases
        if i + iter_i < 0 or i + iter_i >= nb_lines or\
           j + iter_j < 0 or j + iter_j >= nb_cols:
            continue

        # get a multiplier
        multiplier = 1
        res2 = test_empty_2(data, i + iter_i*multiplier, j + iter_j*multiplier)
        while res2 == -1:
            multiplier += 1
            # handle limit cases
            if i + iter_i*multiplier < 0 or i + iter_i*multiplier >= nb_lines or\
               j + iter_j*multiplier < 0 or j + iter_j*multiplier >= nb_cols:
                res2 = 0
                break
            res2 = test_empty_2(
                data, 
                i + iter_i*multiplier, 
                j + iter_j*multiplier
            )
        
        # handle floor
        res += res2

    # get results
    if data[i][j] == "L" and res == 0:
        data_copy[i][j] = "#"
        return True

    if data[i][j] =='#' and res >= 5:
        data_copy[i][j] = "L"
        return True

    return False

def pb2(data):
    data_copy = np.copy(data)
    res = 1
    while res:
        res = 0
        for i in np.arange(nb_lines):
            for j in np.arange(nb_cols):
                if test_neighbours_2(data, data_copy,i,j):
                    res += 1
        data = np.copy(data_copy)
    return data

dt2 = pb2(np.copy(d))
print("Pb 2: ", len(np.where(dt2 == "#")[0]))
import numpy as np
import itertools

def readfile(path, my_type=str):
    with open(path, 'r') as fileObj:
        num = fileObj.read().splitlines()
    num = np.array([my_type(n) for n in num])
    return num


#généralisation du problème
def check_sum(data, value, n=2):
    for tuple in itertools.combinations(data, n):
        if(sum(list(tuple)) == value):
            return True, tuple
    return False, 0


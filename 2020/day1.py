
import numpy as np
import itertools
from utils import readfile
 

# get data
data = readfile(r"2020/day1.txt", my_type=int)

# problème 1
dt = data
for i in data:
    dt = np.delete(dt, 0)
    for j in dt:
        if(i+j == 2020):
            print("premier chiffre", i, 
                "\ndeuxième chiffre", j, 
                "\nproduit", i*j)

# problème 2
for (i, j, k) in itertools.combinations(data, 3):
    if(i+j+k == 2020):
        print("résultat: ", i*j*k)

#généralisation du problème
def check_sum(data, n):
    for tuple in itertools.combinations(data, n):
        if(sum(list(tuple)) == 2020):
            print("résultat: ", np.product(list(tuple)))


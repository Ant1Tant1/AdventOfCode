from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-3.txt", my_type=str)

# -------- FIRST PB -------------------
data = np.array([list(string) for string in data])
data = data.astype(int)
n, width = np.shape(data)

gamma_rate = (data.sum(axis=0)/n > 0.5)
gamma_res = int("".join(map(str, gamma_rate.astype(int))), 2)

epsilon_rate = ~gamma_rate
epsilon_res = int("".join(map(str, epsilon_rate.astype(int))), 2)

print("Gamma rate: ", bin(gamma_res), 
      " Epsilon rate: ", bin(epsilon_res),
      "Results: ", gamma_res * epsilon_res
)

# ---------- SECOND PB --------------
def get_occurence_ox(array, i):
    n = len(array)
    return (array.sum(axis=0)/n)[i] >= 0.5

# type ox = true
# type c02 = false
def get_new_array(array, i, type):
    #print(array)
    bin_condition = ~ (get_occurence_ox(array, i) ^ type)
    c, = np.where(array[:,i] == bin_condition)
    #print(c)
    return array[c]

def recursive(array, type, i = 0):
    if len(array) == 1:
        return array
    return recursive(get_new_array(array, i, type), type, i+1)

r_ox = recursive(data, True)[0]
r_co2 = recursive(data, False)[0]

r_ox = int("".join(map(str, r_ox)), 2)
r_co2 = int("".join(map(str, r_co2)), 2)

print("Ox rate: ", bin(r_ox), 
      " CO2 rate: ", bin(r_co2),
      "Results: ", r_ox * r_co2
)
from utils import readfile, check_sum
import itertools

data = readfile("2020/day9.txt", my_type=int)

# ================================ PB 1 ==========================
def check_sum_reccursive(data, i=0, increment=25):
    if i + increment >= len(data):
        raise ValueError("Did not find an answer")
    getIt, tuple = check_sum(data[i:i+increment], data[i+increment], n=2)
    if not getIt:
        return data[i+increment]
    return check_sum_reccursive(data, i+1, increment)

res = check_sum_reccursive(data, i=0, increment=25)
print("Pb 1: ", res)

# ================================= PB 2 =========================
i = 0
nb_consecutive_values = 2
while sum(data[i:i+nb_consecutive_values]) != res:
    if(i+nb_consecutive_values > len(data)):
        print("Failed for nb consecutive values = ", nb_consecutive_values)
        i = 0
        nb_consecutive_values += 1
        if nb_consecutive_values > len(data):
            break
    i += 1
res2 = min(data[i:i+nb_consecutive_values]) + max(data[i:i+nb_consecutive_values])
print("Success\nPb 2: ", res2)

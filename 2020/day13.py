from utils import readfile
import numpy as np
data = readfile("2020/day13.txt")

# ====================== PB 1 ==================
earliest_time = float(data[0])

bus = data[1].replace(',x', '')
bus = bus.split(',')
bus = np.array(bus, dtype=int)

closest_departure = (earliest_time // bus + 1) * bus - earliest_time

print("Pb 1: ", bus[np.argmin(closest_departure)]* closest_departure.min())

# ====================== PB 2 =======================
scheduler = np.array(data[1].replace('x', '0').split(','), dtype = int)

# get max arg and value to reduce loop iterations   
valmax = scheduler.max()
argmax = scheduler.argmax()

# def method to get next timestamp
get_timestamp = lambda i: valmax * i - argmax

def check_condition(timestamp):
    for i, val in enumerate(scheduler):
        if val == 0:
            continue
        if i == 0 and timestamp % val == 0:
            continue
        if timestamp % val - val + i != 0:
            return False
    return True

# this get the next multiplier to get the modulo value
def find_next_multiplier(multiplier, modulo, value):
    if value < 0 or value > modulo:
        print("ERROR - infinite loop")
    index = 1
    while multiplier * index % modulo != value:
        index += 1
    return index

# get the result by iterating the scheduler values
res = float(1)
multiplier = float(1)
for i, n in enumerate(scheduler):
    if n == 0:
        continue
    # get modulo
    v_modulo = res % n
    # if v_modulo == i:
    #     multiplier *= n
    #     continue

    # get res
    next_mult = find_next_multiplier(multiplier, n, (n - v_modulo - i) % n)
    res += multiplier * next_mult
    multiplier *= n
    print("Line:", i, "\tvalue:", n, "\tActual res =", res)


print("Pb 2: ", res)


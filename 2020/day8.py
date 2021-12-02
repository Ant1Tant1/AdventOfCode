from utils import readfile
import numpy as np
#get data
data = readfile("2020/day8.txt")

# ================================ PB 1 =====================================
def get_value(data, lines_read=np.zeros(len(data), dtype=bool), i=0, res=0):
    if i == 0:
        lines_read=np.zeros(len(data), dtype=bool)
    if i >= len(lines_read):
        return True, res
    if lines_read[i]:
        return False, res

    lines_read[i] = True
    action, value = data[i].split(" ")
    value = int(value)

    if action == "acc":
        return get_value(data, lines_read, i+1, res+value)
    elif action == "jmp":
        return get_value(data, lines_read, i+value, res)
    elif action == "nop":
        return get_value(data, lines_read, i+1, res)

print("Pb 1: ", get_value(data))

# ================================ PB 2 =====================================
def alter_data(count):
    dt = [d for d in data]
    if 'nop' in data[count]:
        dt[count] = data[count].replace('nop', 'jmp')
        return dt
    elif 'jmp' in data[count]:
        dt[count] = data[count].replace('jmp', 'nop')
        return dt
    return []

count = 0
dt = alter_data(count)
if dt == []:
    result = False,
else:
    result = get_value(dt)
while not result[0]:
    count += 1
    dt = alter_data(count)
    if dt == []:
        continue
    result = get_value(dt)

print("Pb 2: ", result)

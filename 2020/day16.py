from utils import readfile
import numpy as np

# read file
data = readfile("2020/day16.txt")

# ============================= PB 1 =======================================
# get the rules
def  get_rules(data):
    dico = {}
    dt = data.copy()
    # loop on data
    for d in data:
        print(d)

        # delete useless rows
        dt = np.delete(dt, 0)

        # stop the loop
        if d == '\n' or d == "":
            break

        # get the rules
        key, values = d.split(": ")
        interval1, interval2 = values.split(" or ")
        interval1 = [int(x) for x in interval1.split("-")]
        interval2 = [int(x) for x in interval2.split("-")]
        dico[key] = np.concatenate(
            [            
            np.arange(interval1[0], interval1[1] + 1),
            np.arange(interval2[0], interval2[1] + 1)
            ]
        )
    
    return dico, dt

# get a dictionary of rules
rules_dict, dt = get_rules(data)

# get unique values in that dict
uniques = np.unique(np.concatenate(list(rules_dict.values())))

# get the data
def get_data(data):
    results = []
    indexer = []
    dt = data.copy()

    # get rid of useless data
    for i, d in enumerate(data):
        #dt = np.delete(dt, 0)
        if d != "nearby tickets:":
            continue
        else:
            break

    i += 1
    for index in range(i, len(data)):
        res = is_line_in_rules(data[index])
        if len(res) != 0:
            results.append(res)
            indexer.append(index)

    return np.concatenate(results), indexer, dt


# get values in rules or not
def is_line_in_rules(line):
    res = []
    values = [int(x) for x in line.split(",")]
    for i, value in enumerate(values):
        if value not in uniques:
            res.append(value)
    return res

# print results
results, indexer, dt = get_data(dt)
print("Pb 1:", results.sum())

# get valid tickets
dt = np.delete(dt, indexer)

# ============================== PB 2 ========================================

# get my ticket
my_ticket = dt[1].split(',')

# get valid nearby tickets
dt = dt[4:]

# nb rules 
nb = len(dt[0].split(','))
arrays = [np.zeros(nb, dtype=bool) for i in range(nb)]

# get non working rules
for d in dt:
    v_rules = [int(x) for x in d.split(",")]
    for i, v_r in enumerate(v_rules):
        for j, values in enumerate(rules_dict.values()):
            if v_r not in values:
                arrays[i][j] = True


# get rule by column 
arg_sorted = np.zeros(nb)
for i, arr in enumerate(arrays):
    arg_sorted[i] = sum(arr)

argSorted = np.argsort(arg_sorted)[::-1][:nb]

result = np.zeros(nb)
for i, index in enumerate(argSorted):
    for j in range(i):
        arrays[index][int(result[argSorted[j]])] = True

    result[index] = np.where(arrays[index] == False)[0][0]

# get results of first 6 inputs
order_res =np.argsort(result)

final_res = float(1)
for index in order_res[:6]:
    final_res *= float(my_ticket[index]) 

print("Pb 2:", final_res)
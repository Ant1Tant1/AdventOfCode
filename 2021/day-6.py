from utils import readfile
import numpy as np
import collections

# read data
data = readfile(r"2021/day-6.txt", my_type=str)

# data = ['3,4,3,1,2']

# split the data
array = data[0].split(',')
data = np.array(array, dtype=int)
data.sort()
c = collections.Counter(data)


# ---------------- FIRST PB ----------------------
# Get fishes for a given timer
def get_fishes(fishDay, timer):
    fish = []
    fish.append(fishDay)
    t = 0
    while t < timer:
        t += 1
        for i in range(len(fish)):
            
            fish[i] -= 1
            if fish[i] < 0:
                fish[i] = 6
                fish.append(8)
    return fish

timer = 80
res = 0
# get the number of fish for each initial condition multiplied by the occurence of that fish
for key, val in c.items():
    res += val * len(get_fishes(key, timer))

print(res)

# ---------------- SECOND PB ----------------------

# precompute collections over a lesser timeframe of timer / DIVIDER = 64 days
timer = 256
DIVIDER = 4
fishCollections = []
for i in range(9):
    array = get_fishes(i, int(timer/DIVIDER))
    array.sort()
    fishCollections.append(collections.Counter(array))

# now implement a recursive method which will be using precalculated collection 
# to avoid computing numerous time the descendant of fishes of same age
res = 0
counter = 0
multiplier = 1
def recursive(col, counter, multiplier):
    global res # global variable
    # loop on the collection items key is the day number, val the number of fish with that day nb
    for key, val in col.items():
        # print("counter: ", counter, "key: ", key, "val: ", val, "multiplier: ", multiplier)
                
        # get precalculated collection of fish after timer / divider = 64 days
        c = fishCollections[key]

        # if counter is reached, add this number of fishes to res 
        if (counter + 1 == DIVIDER):
            res += multiplier * val * sum(c.values()) # multiplier is the val of previous generations
            continue

        # otherwise call the method on next generation 
        recursive(c, counter + 1, multiplier * val)
        
    if counter + 1 == DIVIDER:
        return

# resolve the pb
recursive(c, counter, multiplier)
print(res)


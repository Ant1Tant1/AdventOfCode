from utils import readfile
import numpy as np
import math

data = readfile("2020/day5.txt")

# recursif is life
def get_seat(seq, min, max):
    if len(seq) == 0:
        return min
    
    # apply rules for new min / max
    if seq[0] == 'F' or seq[0] == 'L':
        max = max - math.ceil((max-min)/2)
    if seq[0] == 'B' or seq[0] == 'R':
        min = min + math.ceil((max-min)/2)
        
    #drop first value from seq
    seq = seq.removeprefix(seq[0])

    return get_seat(seq, min, max)


ids = [get_seat(s[:7], 0, 127) * 8 + get_seat(s[7:], 0, 7) for s in data]
ids.sort()

print("Pb 1: ", max(ids))

# get where diff is not 1 (missing number)
missing_id = np.where(np.diff(np.asarray(ids)) != 1)[0][0]

# get the id of this diff and add 1
print("Pb 2: ", ids[missing_id]+1)

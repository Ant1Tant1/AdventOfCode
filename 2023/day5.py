from utils import readfile
import numpy as np

# read data
data = readfile(r"2023/day5.txt")
seeds = [int(i) for i in data[0].split(': ')[1].split()]

maps = []
idx = -1
for line in data[1:]:
    if line == "":
        maps.append([])
        idx += 1
    elif "map" in line:
        pass
    else:
        maps[idx].append([int(i) for i in line.split()])


#=============================== First part ===============================

def apply_map(seed, maps):
    for map in maps:
        for m in map:
            diff = seed - m[1]
            if ((diff >= 0) & (diff < m[2])):
                seed = m[0] + diff
                break
    return seed

locations = [apply_map(seed, maps) for seed in seeds]
print(np.min(locations))

#=============================== Second part ===============================
#From Hugo

def rec_apply_map(seed, map):
    # Stop condition
    if len(map) == 0:
        return [seed]
    # variables
    start, range_ = seed
    dest, source, len_ = map[0]
    transition = dest - source
    # inner overlap
    if (start >= source) & (start+range_ <= source+len_):
        return [(start+transition, range_)]
    # no overlap
    elif (start >= source+len_) | (start+range_ < source):
        return rec_apply_map(seed, map[1:])
    # lower overlap
    elif (start < source) & (start+range_ <= source+len_):
        return [(source+transition, start+range_-source)] + rec_apply_map((start, source-start), map[1:])
    # upper overlap
    elif (start >= source) & (start+range_ > source+len_):
        return [(start+transition, source+len_-start)] + rec_apply_map((source+len_, start+range_-(source+len_)), map[1:])
    # complete overlap
    else:
        return [(source+transition, len_)] + rec_apply_map((start, source-start), map[1:]) + rec_apply_map((source+len_, start+range_-(source+len_)), map[1:])


seeds = [(s,r) for s,r in zip(seeds[::2], seeds[1::2])]
for map in maps:
    next_seeds = []
    for seed in seeds:
        next_seeds.extend(rec_apply_map(seed, map))
    seeds = next_seeds

locations = [seed[0] for seed in seeds]
print(np.min(locations))
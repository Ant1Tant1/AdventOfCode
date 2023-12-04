from utils import readfile
import numpy as np
import re

# read data
data = readfile(r"2023/day3.txt")

regex = re.compile('[0-9]+')
numbers = [regex.findall(line) for line in data]
numbers.insert(0,[])
numbers.append([])

padded_data = np.array([list(string) for string in data])
padded_data = np.pad(padded_data, 1, "constant", constant_values='.')
i, j = padded_data.shape


def is_adjacent_to_a_symbol(i, j_start, j_end):
    for idx in range(i-1, i+2):
        # print(idx)
        for j in range(j_start-1, j_end+2):
            # print("j ", j)
            if padded_data[idx, j] != "." and not (idx == i and j >= j_start and j <= j_end):
                return True
    return False

results = []
for idx in range(i):
    j_end = 0
    results.append([])
    for nb in numbers[idx]:
        n = len(nb)

        for col in range(j_end, j):
            if padded_data[idx, col] == nb[0]:
                results[idx].append(
                    is_adjacent_to_a_symbol(idx, col, col+n-1)
                )
                j_end = col + n
                break

res = 0
for result, number in zip(results, numbers):
    for b, nb in zip(result, number):
        if b:
            res += int(nb)

print("Problem 1: ", res)




stars = np.zeros([i, j])
gear_ratio = np.ones([i, j])
def is_adjacent_to_a_star(i, j_start, j_end, nb):
    for idx in range(i-1, i+2):
        for j in range(j_start-1, j_end+2):
            if padded_data[idx, j] == "*":
                stars[idx, j] += 1
                gear_ratio[idx, j] *= nb



for idx in range(i):
    j_end = 0
    results.append([])
    for nb in numbers[idx]:
        n = len(nb)
        for col in range(j_end, j):
            if padded_data[idx, col] == nb[0]:
                is_adjacent_to_a_star(idx, col, col+n-1, int(nb))
                j_end = col + n
                break

print("Problem 2: ", gear_ratio[stars == 2].sum())
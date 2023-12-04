from utils import readfile
import numpy as np
import re

# read data
data = readfile(r"2023/day4.txt")
regex = re.compile('[0-9]+')

def get_len_of_matching_numbers(line):
    winning_nb, my_number = line.split(': ')[1].split(" | ")
    winning_nb = set([int(w) for w in regex.findall(winning_nb)])
    my_number = set([int(nb) for nb in regex.findall(my_number)])
    inter = my_number.intersection(winning_nb)
    return len(inter)

res = 0
for line in data:
    lenght = get_len_of_matching_numbers(line)
    if lenght != 0:
        res += 2**(lenght - 1)

print("Problem 1: ", res)


cards = np.ones(len(data))
for i, line in enumerate(data):
    lenght = get_len_of_matching_numbers(line)

    while lenght != 0:
        cards[i+lenght] += cards[i]
        lenght-=1

print("Problem 2: ", cards.sum())
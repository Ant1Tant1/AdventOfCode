from itertools import count
import numpy as np
import itertools
from utils import readfile


# get data
data = readfile(r"2020/day2.txt")

def get_value(d):
    bornes, letter, password = d.split(' ')
    letter = letter.split(":")[0]
    bornesInf, borneSup= [int(n) for n in bornes.split('-')]
    return bornesInf, borneSup, letter, password

def is_password_valid(*args):
    return True if args[3].count(args[2])>=args[0] and args[3].count(args[2])<=args[1] else False


def is_password_valid2(*args):
    return True if (
                    args[3][args[0]-1]==args[2] 
                    and args[3][args[1]-1]!=args[2]
                ) or (
                    args[3][args[0]-1]!=args[2] 
                    and args[3][args[1]-1]==args[2]
                ) else False
        
print("Number of correct passwords: ")
print("Method 1: ",
      sum([is_password_valid(*get_value(d)) for d in data])
)

print("Method 2: ",
      sum([is_password_valid2(*get_value(d)) for d in data])
)


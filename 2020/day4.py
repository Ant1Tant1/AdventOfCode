import numpy as np
from utils import readfile
import re

# get data
data = readfile(r"2020/day4.txt")

def format_data(data):
    l = list()
    d = {}
    for line in data:
        if line == "":
            l.append(d)
            d = {}
        else:
            entries = line.split(" ")
            for entry in entries:
                key, value = entry.split(":")
                d[key] = value
    #last value
    l.append(d)
    return l

#format data
data = format_data(data)

#check validity
keys = ["byr", "iyr", "eyr", "hgt",
        "hcl", "ecl", "pid", "cid"]

keys_not_to_check = ["cid"]

# remove key not to check
for key_to_remove in keys_not_to_check:
    if key_to_remove in keys:
         keys.remove(key_to_remove)


result = [True if all(key in dt.keys() for key in keys) else False for dt in data]
print("Pb 1: ", sum(result))


# validate value
def validate_value(key, value):
    if key == "byr":
        try:     

            return True if int(value) <= 2002 and int(value) >=1920 \
            else False
        except:
            return False
    elif key == "iyr":
        try:
            return True if int(value) >= 2010 and int(value) <= 2020 \
            else False
        except:
            return False            
    elif key == "eyr":
        try:
            return True if int(value) >= 2020 and int(value) <= 2030 \
            else False
        except:
            return False       
    elif key == "hgt":
        if(value[-2:] == 'cm'):
            try:
                return True if int(value[:-2]) >= 150 and int(value[:-2]) <= 193 \
                else False
            except:
                return False
        elif(value[-2:] == 'in'):
            try:
                return True if int(value[:-2]) >= 59 and int(value[:-2]) <= 76 \
                else False
            except:
                return False    
        else:
            return False
    elif key == "hcl":
        if(value[0] != '#'):
            return False
        if(len(value) != 7):
            return False
        pattern = re.compile("[a-z0-9]+")
        return True if pattern.fullmatch(value[1:]) else False
    elif key == "ecl":
        return True \
            if(value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) \
            else False
    elif key == "pid":
        if(len(value) != 9):
            return False
        pattern = re.compile("[0-9]+")
        return True if pattern.fullmatch(value) else False
    elif key == "cid":
        return True


# check validity of values
result2 = np.ones(len(result),dtype=bool)
for i, dt in enumerate(data):
    # avoid number whose keys are wrong
    if not result[i]:
        result2[i] = 0
        continue

    for key, value in dt.items():
        if(validate_value(key, value)):
            continue
        else:
            result2[i] = 0
            break
print("Pb 2: ", result2.sum())



    

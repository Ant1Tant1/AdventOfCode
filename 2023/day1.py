from utils import readfile
import numpy as np
import re

# read data
data = readfile(r"2023/day1.txt")


# problem 1
regex = re.compile('[0-9]')

results = np.zeros(len(data))
for i, line in enumerate(data):
    nb = regex.findall(line)
    results[i] = int("".join([nb[0], nb[-1]]))

# other option - more elegant but longer
digits = [''.join(re.findall(r'\d+', i)) for i in data]
lasttwo_digits = [int(f'{d[0]}{d[-1]}') for d in digits]

print(results.sum(), sum(lasttwo_digits))


# problem 2
regex = re.compile(
    'eighthree|eightwo|sevenine|twone|eightwo|oneight|threeight|fiveight|nineight|' +
    'one|two|three|four|five|six|seven|eight|nine|' +
    '[0-9]'
)

def transform(txt):

    str_to_nb = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8",
        "nine": "9",
        "eighthree" : "83",
        "eightwo": "82",
        "sevenine" : "79",
        "twone": "21",
        "oneight": "18",
        "threeight": "38",
        "fiveight":"58",
        "nineight":"98"
    }

    if len(txt) == 1:
        return txt

    return str_to_nb[txt]


results = np.zeros(len(data))
for i, line in enumerate(data):
    nb = regex.findall(line)

    results[i] = int("".join([transform(nb[0]), transform(nb[-1])]))

    if results[i] > 100:
        results[i] = results[i]//100*10 + results[i]%10
        # print(line)
        # print(nb)
        # print(results[i])

print(results.sum())

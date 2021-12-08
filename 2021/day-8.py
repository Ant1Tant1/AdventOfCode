from numpy.core.fromnumeric import transpose
from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-8.txt", my_type=str)

data = [i.split(' | ')[1].split(" ") for i in data]
data = np.asarray(data)


# ===========  PB 1  ===========
# create a dict of combination value / nb of elements
easy_comb_dict = {1:2, 4:4, 7:3, 8:7}

# if len of element is in the dict, set to true and sum for result
r = [len(dt) in easy_comb_dict.values() for dt in data.reshape(-1)]
print(np.sum(r), "are part of the digits", easy_comb_dict.keys())


# ===========  PB 2  ===========
# could have been solved a better way .. 
array = np.asarray([1, 7, 4, 2,3,5, 0,6,9, 8])
dict_result = {"abcefg": 0, 'cf': 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}
class Data:
    def __init__(self, line):
        self.entries = np.asarray(line.split(' | ')[0].split(" "))
        self.entries = np.asarray(sorted(self.entries, key=len))
        self.results = np.asarray(line.split(' | ')[1].split(" "))
        self.letter_dict = {}
        
        # a is the diff between nb 1 & 7 which are entries 0 & 1 
        self.letter_dict['a'] = (set(self.entries[0]) ^ set(self.entries[1])).pop() # difference

        # g is the diff between 4a & 9 
        self.letter_dict['g'] = sorted(
            [set(self.letter_dict['a'] + self.entries[2]) ^ set(s) for s in self.entries[6:9]], 
            key=len
        )[0].pop()

        # d is the diff between 1ag & 3
        self.letter_dict['d'] = sorted(
            [set(self.letter_dict['a'] + self.letter_dict['g'] + self.entries[0]) 
            ^ set(s) for s in self.entries[3:6]],
            key=len
        )[0].pop()

        # b is the diff between 1d & 4
        self.letter_dict['b'] = (set(self.entries[0] + self.letter_dict['d']) ^ set(self.entries[2])).pop()

        # f is the diff between abdg & 5
        self.letter_dict['f'] = sorted(
            [set(self.letter_dict['a'] + self.letter_dict['b'] + self.letter_dict['d'] + self.letter_dict['g']) 
            ^ set(s) for s in self.entries[3:6]],
            key=len
        )[0].pop()

        # c is the diff between 1 & f
        self.letter_dict['c'] = (set(self.letter_dict['f']) ^ set(self.entries[0])).pop()

        # e is the diff between 8 & abcdfg
        self.letter_dict['e'] = (set(self.letter_dict['a'] + self.letter_dict['b'] + self.letter_dict['c'] 
            + self.letter_dict['d'] + self.letter_dict['f'] + self.letter_dict['g']) 
            ^ set(self.entries[9])
        ).pop()

        self.transposed_dict_res = {self.transpose(key):value for key, value in dict_result.items()}
        
    def transpose(self, key):
        key_array = [self.letter_dict[letter] for letter in key]
        return "".join(sorted(key_array))

    def get_result(self):
        res_array = np.asarray([self.transposed_dict_res["".join(sorted(res))] for res in self.results], dtype=str)
        return int("".join(res_array))

# read data
data = readfile(r"2021/day-8.txt", my_type=str)

d = np.asarray([Data(dt) for dt in data])
results = [dt.get_result() for dt in d]
print(sum(results))
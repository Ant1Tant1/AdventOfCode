from os import read
from utils import readfile

#get data
data = readfile("2020/day7.txt")

def get(x):
    key, values = x.split(" bags contain")
    if "no other" in values:
        return key, [], []
    val = values.split(",")
    value = [v.split(" bag")[0][3:] for v in val]
    nb = [int(v[1]) for v in val]
    return key, value, nb

def get_bags(data):
    return [get(x) for x in data]

#create a dict of key and links
names_dict = {key:value for key, value, nb in get_bags(data)}
nbs_dict = {key:nb for key,value, nb in get_bags(data)}

# ============================ PROBLEM 1 ================================
# instantiate a dict of results
results = {key:0 for key in names_dict.keys()}

def find_key(key, bag_to_hold="shiny gold"):
    for value in names_dict[key]:
        # if the bag to hold is in value return 1
        if value == bag_to_hold:
            return 1
        # if we already know one of the bags can hold our bag -> true
        if results[key] == 1:
            return 1
        # get reccursive result
        if find_key(value, bag_to_hold) == 1:
            return 1
    # bag has not be found
    return 0
        
for key in results.keys():
    results[key] = find_key(key, bag_to_hold="shiny gold")
print("Pb 1: ", sum(list(results.values())))

# ============================ PROBLEM 2 ================================
def find_nb_bags(key="shiny gold"):
    res = 0
    for bag_name, bag_nb in zip(names_dict[key], nbs_dict[key]):
        res += bag_nb*(1+find_nb_bags(bag_name))
    return res
print("Pb 2: ", find_nb_bags(key="shiny gold"))

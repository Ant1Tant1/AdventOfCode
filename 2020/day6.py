from utils import readfile
# get data
data = readfile("2020/day6.txt")
# ================================== FIRST PART ===================================
dt = [""]
for d in data:
    if d == '':
        dt.append("")
    else:
        dt[len(dt)-1] += d

# Function to remove all duplicates from string  
# and order does not matter  
def removeDupWithoutOrder(str):   
    return "".join(sorted(set(str)))


dt = [removeDupWithoutOrder(d) for d in dt]

s = [len(d) for d in dt]

print("Pb 1: ", sum(s))

# ================================ SECOND PART =======================================
def get_intersection(str1, str2):
    return "".join(set.intersection(*[set(str1), set(str2)]))

dt = [""]
first = True
for d in data:
    if d == "":
        dt.append("")
        first = True
    elif first:
        dt[len(dt)-1] += d
        first = False
    else:
        # remove the ones that are not in d
        dt[len(dt)-1] = get_intersection(dt[len(dt)-1], d)

s = [len(d) for d in dt]

print("Pb 2: ", sum(s))
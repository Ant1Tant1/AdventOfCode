from utils import readfile
import numpy as np

# read data
data = readfile(r"2022/day8.txt")

height = len(data)
width = len(data[0])

input = np.zeros([height, width])
for i, line in enumerate(data):
    for j, char in enumerate(line):
        input[i, j] = int(char)

res1 = np.zeros([height, width], dtype=bool)

def return_visible(array):
    max_size = -1
    res = np.zeros(len(array), dtype=bool)
    for i, val in enumerate(array):
        if val > max_size:
            max_size = val
            res[i] = True
    return res

for i in range(height):
    res1[i,:] |= return_visible(input[i,:])
    res1[i,:] |= return_visible(input[i,::-1])[::-1]

for j in range(width):
    res1[:,j] |= return_visible(input[:,j])
    res1[:,j] |= return_visible(input[::-1,j])[::-1]

print("first pb: ", np.sum(res1))

res2 = np.zeros([height, width])


def get_score(i, j):  
    score = np.ones(4)  
    # to the right
    counter = 1
    while counter + i < width - 1 :
        if input[i, j] > input[i+counter, j]:
            counter += 1
        else:
            break
    score[0] = counter

    # to the left
    counter = -1
    while counter + i > 0:
        if input[i, j] > input[i+counter, j]:
            counter -= 1
        else:
            break
    score[1] = -counter

    # up 
    counter = -1
    while counter + j > 0:
        if input[i, j] > input[i, j+counter]:
            counter -= 1
        else:
            break
    score[2] = -counter

    # down
    counter = 1
    while counter + j < height - 1:
        if input[i, j] > input[i, j+counter]:
            counter += 1
        else:
            break
    score[3] = counter
    
    return np.prod(score)


for i in range(1, height-1):
    for j in range(1, width-1):
        if res1[i, j]:
            print(res1[i,j], input[i,j], i , j)
            res2[i,j] = get_score(i, j)


print("second pb: ", np.max(res2))    

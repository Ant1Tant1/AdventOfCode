from utils import readfile
import numpy as np

# read data
data = readfile(r"day5.txt")

def create_stack():
    idx = -1
    stacks = [[] for i in range(9)]

    for line in data:
        idx += 1
        if line == ' 1   2   3   4   5   6   7   8   9 ':
            break

        stack_idx = 0
        counter = 0
        for c in line.split(' '):
            if counter == 4:
                stack_idx += 1
                counter = 0

            if c == "":
                counter += 1
                continue
            
            stacks[stack_idx].insert(0, c[1])
            stack_idx += 1
    return stacks

stacks = create_stack()
for line in data[10:]:
    _, number, _, stack_from, _, stack_to = line.split(' ')
    for i in range(int(number)):
        obj = stacks[int(stack_from)-1].pop()
        stacks[int(stack_to)-1].append(obj)


print("first pb: ", "".join([stack[-1] for stack in stacks]))

stacks = create_stack()
for line in data[10:]:
    _, number, _, stack_from, _, stack_to = line.split(' ')
    obj = []
    for i in range(int(number)):
        obj.append(stacks[int(stack_from)-1].pop())

    for o in obj[::-1]:
        stacks[int(stack_to)-1].append(o)

print("second pb: ", "".join([stack[-1] for stack in stacks]))

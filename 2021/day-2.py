from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-2.txt", my_type=str)


# -------- FIRST PB -------------------
horizontal_position = 0
depth = 0

for move in data:
    move_type, value = move.split(" ")
    if move_type == "forward":
        horizontal_position += int(value)
    elif move_type == "up":
        depth -= int(value)
    elif move_type == "down":
        depth += int(value)
    else:
        raise Exception("Type of movement not known")

result = horizontal_position * depth
print(result)

# ---------- SECOND PB --------------
horizontal_position = 0
depth = 0
aim = 0

for move in data:
    move_type, value = move.split(" ")
    if move_type == "forward":
        horizontal_position += int(value)
        depth += aim * int(value)
    elif move_type == "up":
        aim -= int(value)
    elif move_type == "down":
        aim += int(value)
    else:
        raise Exception("Type of movement not known")

result = horizontal_position * depth
print(horizontal_position, depth, result)


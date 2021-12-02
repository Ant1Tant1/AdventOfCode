from utils import readfile
import numpy as np
from math import sin, cos

data = readfile("2020/day12.txt")


dir_x = 0
dir_y = 0
facing_dir = 0

def get_action(i=0, facing_dir=0, dir_x=0, dir_y=0):
    if i >= len(data):
        return abs(dir_x) + abs(dir_y) 

    char = data[i][0]
    value = float(data[i][1:])
    if char == 'N':
        dir_y += value
    elif char == 'S':
        dir_y -= value
    elif char == 'E':
        dir_x += value
    elif char == 'W':
        dir_x -= value
    elif char == 'R':
        facing_dir -= value
    elif char == 'L':
        facing_dir += value
    elif char == 'F':
        dir_y += round(sin(facing_dir*math.pi/180) * value, 1)
        dir_x += round(cos(facing_dir*math.pi/180) * value, 1)
    
    return get_action(i+1, facing_dir, dir_x, dir_y)

print("Pb 1: ", get_action())

def get_action_2(i=0, ship_pos=np.array([0,0]), dir=np.array([10,1])):
    if i >= len(data):
        return (np.abs(ship_pos)).sum()

    char = data[i][0]
    value = float(data[i][1:])
    if char == 'N':
        dir[1] += value
    elif char == 'S':
        dir[1] -= value
    elif char == 'E':
        dir[0] += value
    elif char == 'W':
        dir[0] -= value
    elif char == 'R':
        new_x = (dir[0] * cos(-value*math.pi/180) - dir[1] * sin(-value*math.pi/180))
        new_y = (dir[0] * sin(-value*math.pi/180) + dir[1] * cos(-value*math.pi/180))
        dir = [round(new_x, 1), round(new_y, 1)]
    elif char == 'L':
        new_x = (dir[0] * cos(value*math.pi/180) - dir[1] * sin(value*math.pi/180))
        new_y = (dir[0] * sin(value*math.pi/180) + dir[1] * cos(value*math.pi/180))
        dir = [round(new_x, 1), round(new_y, 1)]
    elif char == 'F':
        ship_pos[0] = ship_pos[0] + value * dir[0]
        ship_pos[1] = ship_pos[1] + value * dir[1]

    #print(ship_pos, dir)
    return get_action_2(i+1, ship_pos, dir)

print("Pb 2: ", get_action_2())
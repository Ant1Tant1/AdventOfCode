from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-17.txt", my_type=str)
data = data[0]

# data = "target area: x=20..30, y=-10..-5"

# get data
xborders = [float(x) for x in data.split(',')[0].split('=')[1].split("..")]
yborders = [float(y) for y in data.split(',')[1].split('=')[1].split("..")]

# ==== PB 1

# get x' min and max values
delta = lambda c: 1 + 4*c
value = lambda c: (-1 + np.sqrt(delta(2*c))) / 2


# Useless for pb 1 
# get integer values within x_vel
x_vel_borders = [np.ceil(value(x)) for x in xborders]
x_vels = [x for x in range(int(x_vel_borders[0]), int(x_vel_borders[1]))]


# find lambda values
sum_n = lambda n: n*(n+1)/2

# since i don't know which value will be the biggest I am looping on a lot 
# of values and taking the biggest one that actually works

# the way it is computed is that the highest point sum_n(y_vel) 
# give a new 0 to know if the probe will pass in the right zone
# then you use n*(n+1)/2 to compute the n that works for the min
# and the max y borders. If you have a n integer in between the 
# y_vel_borders, it works, otherwise it does not.
y_vel = 0
possible_yvel = []
while y_vel < 1000:
    y_vel += 1
    y_vel_borders =  [value(-y + sum_n(y_vel)) for y in yborders]
    if (np.ceil(y_vel_borders[0]) == np.ceil(y_vel_borders[1])) & (int(y_vel_borders[0]) == int(y_vel_borders[1])):
        continue
    else:
        possible_yvel.append(y_vel)

print(sum_n(np.max(possible_yvel)))

# ==== PB 2
# compute x at step k for a given x vel  
get_x = lambda x, k: (2*x - k)*(k+1)/2 if x - k > 0 else x*(x+1)/2
# get y border when y values are < 0
get_y_border = lambda b, c: (-b + np.sqrt(b**2 - 4*c)) / 2 


# dimished the number of loop
ymin = int(np.min(yborders))
ymax = int(np.max(possible_yvel))
xmin = int(np.min(x_vels))
xmax = int(np.max(xborders))

# loop 
couples = []
for y_vel in range(ymin, ymax+1):

    if y_vel > 0:
        # get borders for y > 0
        y_vel_borders =  [y_vel + 1 + value(-y + sum_n(y_vel)) for y in yborders]
    else:
        # get borders for y < 0
        y_vel_borders =  [1 + get_y_border(1-2*y_vel, 2*(y - y_vel)) for y in yborders]

    # check if it works for y 
    if (np.ceil(y_vel_borders[0]) == np.ceil(y_vel_borders[1])) & (int(y_vel_borders[0]) == int(y_vel_borders[1])):
        continue
    
    if y_vel_borders[0] - int(y_vel_borders[0]) == 0:
        y_vel_borders[0] +=0.1

    # loop through x vel
    for x_vel in range(xmin, xmax+1):
        # loop through k steps where y is in borders
        for k in range(int(np.ceil(y_vel_borders[1])), int(np.ceil(y_vel_borders[0]))):
                if xborders[0] <= get_x(x_vel, k-1) <= xborders[1]:
                    print(x_vel, y_vel, k)
                    print(get_x(x_vel, k), xborders)
                    couples.append((x_vel, y_vel))
                    break


len(couples)
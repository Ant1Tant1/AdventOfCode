from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-1.txt", my_type=int)

# first problem
diff = np.diff(data)
result = (diff > 0).sum()
print(result)

# second problem
# roll the diff vector and sum it to get the 3 samples window
# then take all values unless the last two (which are wrong due to the rolling)
diff_sum = (diff + np.roll(diff, -1) + np.roll(diff, -2))[:-2]
result = (diff_sum > 0).sum()
print(result)
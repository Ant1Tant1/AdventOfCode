from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-4.txt", my_type=str)

#get nbs 
numbers = np.asarray(data[0].split(','), dtype=int)

# board size
BOARD_SZ = 5

# ------------  get data  ------------------
board_nb = -1
boards = []
for line in data[1:]:
    if(line == ''):
        board_nb += 1
        boards.append(np.zeros((5,5), dtype=int))
        counter = 0
    
    else:
        boards[board_nb][counter] = line.split()
        counter += 1

# -------- FIRST PB -------------------
res = 0
for nb in numbers:
    for board in boards:
        board[board == nb] = -1

        if -BOARD_SZ in board.sum(axis=1) or -BOARD_SZ in board.sum(axis=0):
            res = nb * board[board != -1].sum()
            break
    if (res != 0):
        break

print(res)


# -------- SECOND PB -------------------
res = []
for board in boards:
    for i, nb in enumerate(numbers):
        board[board == nb] = -1
        if -BOARD_SZ in board.sum(axis=1) or -BOARD_SZ in board.sum(axis=0):
            res.append([i, nb * board[board != -1].sum()])
            break

res = np.reshape(res, (-1, 2))
imax = res[:,0].argmax()
print (res[imax])
from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-20.txt", my_type=str)

# data = [
#     "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#",
#     "",
#     "...............",
#     "...............",
#     "...............",
#     "...............",
#     "...............",
#     ".....#..#......",
#     ".....#.........",
#     ".....##..#.....",
#     ".......#.......",
#     ".......###.....",
#     "...............",
#     "...............",
#     "...............",
#     "...............",
#     "..............."
# ]

# get decoder
decoder = data[0]

# read data
data = np.asarray([list(string) for string in data[2:]])

# get first df with 0 and 1
df = np.zeros(data.shape, dtype=int)
df[np.where(data == '#')] = 1

def algorithm(i, j, df):
    binary = "".join([str(c) for c in df[i-1:i+2, j-1:j+2].reshape(1,-1)[0]])
    val = int(binary, 2)
    return get_decoder_val(val)

def get_decoder_val(i):
    if decoder[i] == '.': return 0
    elif decoder[i] == '#': return 1
    else: print("error")

previous_cst = 0
for _ in range(50):
    # THIS WAS ANNOYING
    # YOU HAVE TO GET THE BORDER VALUES DEPENDING OF WHAT THEY BECAME LAST RUN
    # Beginning is only 0
    # after first round they all change to the value of decoder['000000000'] (for _ == 1)
    # after second round they all change to value of decoder['xxxxxxxxx'] with x = decoder['000000000'] 
    if _ > 0:
        previous_cst = get_decoder_val(0) if previous_cst == 0 else get_decoder_val(len(decoder)-1)

    # pad
    df = np.pad(df, 2, constant_values=previous_cst)

    # define res
    res = np.zeros(df.shape, dtype=int)

    # loop trough data only inside previous borders (1, n-1)
    for i in range(1, df.shape[0]-1):
        for j in range(1, df.shape[1]-1):
            res[i, j] = algorithm(i, j, df)

    # crop res
    res = res[1:-1, 1:-1]
    # crop
    df = res.copy()

res
print(len(np.where(res == 1 )[0]))
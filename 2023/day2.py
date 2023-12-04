from utils import readfile
import numpy as np

# read data
data = readfile(r"2023/day2.txt")

results = []
for line in data:
    for set in line.split(": ")[1].split("; "):
        cubes = set.split(' ')
        for i in range(len(cubes)//2):
            # print(cubes)
            if "red" in cubes[2*i+1] and int(cubes[2*i]) > 12:
                results.append(
                    int(
                        line.split(": ")[0].split(' ')[1]
                    )
                )
                break

            if "green" in cubes[2*i+1] and int(cubes[2*i]) > 13:
                results.append(
                    int(
                        line.split(": ")[0].split(' ')[1]
                    )
                )
                break

            if "blue" in cubes[2*i+1] and int(cubes[2*i]) > 14:
                results.append(
                    int(
                        line.split(": ")[0].split(' ')[1]
                    )
                )
                break

print("results: ", np.arange(1, len(data) + 1).sum() - np.sum(np.unique(results)))


results = np.zeros(len(data))
for idx, line in enumerate(data):
    red = green = blue = 0

    for set in line.split(": ")[1].split("; "):
        cubes = set.split(' ')

        for i in range(len(cubes)//2):
            # print(cubes)
            if "red" in cubes[2*i+1] and int(cubes[2*i]) > red:
                red = int(cubes[2*i])

            if "green" in cubes[2*i+1] and int(cubes[2*i]) > green:
                green = int(cubes[2*i])

            if "blue" in cubes[2*i+1] and int(cubes[2*i]) > blue:
                blue = int(cubes[2*i])

    # print(idx, red, green, blue)
    results[idx] = red*green*blue

print("results: ", results.sum())
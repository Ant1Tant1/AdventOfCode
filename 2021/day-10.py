from utils import readfile
import numpy as np

# read data
data = readfile(r"2021/day-10.txt", my_type=str)

# data = [
#     "[({(<(())[]>[[{[]{<()<>>",
#     "[(()[<>])]({[<{<<[]>>(",
#     "{([(<{}[<>[]}>{[]{[(<()>",
#     "(((({<>}<{<{<>}{[]{[]{}",
#     "[[<[([]))<([[{}[[()]]]",
#     "[{[{({}]{}}([{[{{{}}([]",
#     "{<[[]]>}<{[{[{[]{()[[[]",
#     "[<(<(<(<{}))><([]([]()",
#     "<{([([[(<>()){}]>(<<{{",
#     "<{([{{}}[<[[[<>{}]]]>[]]"
# ]

# ===========  PB 1 & 2  ===========
opn_end_char_dict = {'[': ']', '{': '}', '<': '>', '(': ')'}
score_dict = {
    ')': 3,  
    ']': 57,
    '}': 1197,
    '>': 25137,
}

autocomplete_score_dict = {
    ')': 1,  
    ']': 2,
    '}': 3,
    '>': 4,
}

# non corrupted lines are all incompletes
results = []
res1 = 0
for line in data:
    last_open_char = []
    should_continue = False
    for c in line:
        if c in opn_end_char_dict.keys():
            last_open_char.append(c)
        elif c != opn_end_char_dict[last_open_char.pop()]:
            res1 += score_dict[c]
            should_continue = True
            break
    if should_continue: continue
    last_open_char.reverse()
    res = 0
    for i in last_open_char: 
        res = 5*res + autocomplete_score_dict[opn_end_char_dict[i]]
    results.append(res)

print("Pb 1:", res1, "\nPb 2:", int(np.median(results)))
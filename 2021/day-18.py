from utils import readfile
import numpy as np
from ast import literal_eval
import itertools


class PairObj:
    def __init__(self, pair, level=1, parent=None):
        self.pair = []
        self.parent = parent
        self.level = level

        for p in pair:
            if type(p) == int:
                self.pair.append(p)
            
            elif type(p) == PairObj:
                self.pair.append(PairObj(p.pair, self.level+1, self))

            else:
                self.pair.append(PairObj(p, self.level + 1, self))

    def add(self, pairObj):
        new_pair = []
        new_pair.append(self.pair)
        new_pair.append(pairObj)
        return PairObj(new_pair)

    def __repr__(self):
        return f"{self.pair}"
 
    def __str__(self):
        return f"{self.pair}"       

    def reduce(self):
        while 1:
            # print(self)
            explosed = False
            splitted = False
            
            explosed = self.explose()
            if explosed: 
                # print("Explose")
                continue

            splited = self.split()
            if splited: 
                # print("Split")
                continue
            else: break

    def explose(self):
        if self.level != 5:
            for i, p in enumerate(self.pair):
                if type(p) == int:
                    continue
                done = p.explose()
                if p.level == 5:
                    self.pair[i] = 0
                if done:
                    return True
        else:
            self.parent.add_number(self.pair[0], 0, self)
            self.parent.add_number(self.pair[1], 1, self)
            return True

    def add_number(self, nb, dir, child, reverse=False):
        # 0 for left
        # 1 for right
        if type(self.pair[dir]) == int:
            self.pair[dir] += nb

        elif self.pair[dir] != child:
            if reverse:
                self.pair[dir].add_number(nb, dir, self, reverse=True)
            else:
                self.pair[dir].add_number(nb, 1-dir, self, reverse=True)

        elif (self.parent != None) & (self.pair[dir] == child):
            self.parent.add_number(nb, dir, self)

    def split(self):
        done=False
        for i, p in enumerate(self.pair): 
            if type(p) != int:      
                done = p.split()

            elif p >= 10:
                self.pair[i] = PairObj(
                    [p // 2, int(np.ceil(p/2))], 
                    level=self.level+1,
                    parent=self
                )
                return True

            if done:
                return True

    magn = [3, 2]
    def magnitude(self):
        res = 0
        for i, p in enumerate(self.pair): 
            if type(p) == int:      
                res += self.magn[i] * p

            else:
                res += self.magn[i] * p.magnitude()
        return res




# line = "[[[[[9,8],1],2],3],4]"
# line = "[7,[6,[5,[4,[3,2]]]]]"
# line = "[[6,[5,[4,[3,2]]]],1]"
# line = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
# line = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
# line = literal_eval(line)

# data = [
# "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
# "[[[5,[2,8]],4],[5,[[9,9],0]]]",
# "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
# "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
# "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
# "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
# "[[[[5,4],[7,7]],8],[[8,3],8]]",
# "[[9,3],[[9,9],[6,[4,9]]]]",
# "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
# "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"
# ]

# # read data
data = readfile(r"2021/day-18.txt", my_type=str)

# === PB 1
pair = PairObj(literal_eval(data[0]))
pair.reduce()
for d in data[1:]:
    pair = pair.add(literal_eval(d))
    pair.reduce()

print(pair.magnitude())

# === PB 2
res = []
for (i, j) in itertools.permutations(data, 2):
    pair = PairObj([literal_eval(i),literal_eval(j)])
    pair.reduce()
    res.append(pair.magnitude())

print(np.max(res))  
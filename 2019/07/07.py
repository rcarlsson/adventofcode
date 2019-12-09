import sys
import os
from itertools import permutations

sys.path.append('../')
import intcode

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

init_prog = [int(x) for x in open(file_name).read().split(',')]

res1 = 0
for p in permutations([0,1,2,3,4]):
    res = 0
    for i in range(5):
        res = intcode.run(init_prog[:], [p[i], res])[0]

    res1 = max(res1, res)

print("Part 1: {}".format(res1))

res2 = 0
for p in permutations([5,6,7,8,9]):
    res = 0
    tmp_res = 0
    prog = [init_prog[:] for _ in range(5)]
    ip = [0 for _ in range(5)]
    inp = [[p[i]] for i in range(5)]
    while tmp_res is not None:
        for i in range(5):
            inp[i].append(res)
            (tmp_res, ip[i], _) = intcode.run(prog[i], inp[i], ip[i])
            res = res if tmp_res is None else tmp_res
    res2 = max(res2, res)

print("Part 2: {}".format(res2))

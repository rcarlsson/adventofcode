import sys
import os
from itertools import permutations

sys.path.append('../')
from intcode import *

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

program = [int(x) for x in open(file_name).read().split(',')]

res1 = 0
for p in permutations([0,1,2,3,4]):
    res = 0
    for i in range(5):
        c = IntCode(program, [p[i], res])
        c.run()
        res = c.get_out()[0]

    res1 = max(res1, res)

print("Part 1: {}".format(res1))

res2 = 0
for p in permutations([5,6,7,8,9]):
    amps = [IntCode(program, [x]) for x in p]
    amps[0].give_inp(0)
    i = 0
    while amps[i].run() != Result.HALT:
        i_next = (i+1)%len(p)
        amps[i_next].give_inp(amps[i].get_out()[-1])
        i = i_next

    res2 = max(res2, amps[-1].get_out()[-1])

print("Part 2: {}".format(res2))

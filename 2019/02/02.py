import sys
import os
import operator

sys.path.append('../')
from intcode import *

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

program = [int(x) for x in open(file_name).read().split(',')]

c = IntCode([program[0], 12, 2] + program[3:])
c.run()
print("Part 1: {}".format(c.get_reg(0)))

for x in range(100):
    for y in range(100):
        c = IntCode([program[0], x, y] + program[3:])
        c.run()
        if (c.get_reg(0) == 19690720):
            print("Part 2: {}".format(100*x + y))
            exit(0) 

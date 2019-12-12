import sys
import os
from itertools import permutations

sys.path.append('../')
from intcode import *

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

program = [int(x) for x in open(file_name).read().split(',')]

c = IntCode(program,[1])
c.run()
print("Part 1: {}".format(c.get_out()[0]))
c = IntCode(program,[2])
c.run()
print("Part 2: {}".format(c.get_out()[0]))

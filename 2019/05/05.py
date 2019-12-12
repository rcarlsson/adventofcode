import sys
import os

sys.path.append('../')
from intcode import *

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

program = [int(x) for x in open(file_name).read().split(',')]

c = IntCode(program,[1])
while c.run() != Result.HALT: {}
print("Part 1: {}".format(c.get_out()[-1]))
c = IntCode(program,[5])
while c.run() != Result.HALT: {}
print("Part 2: {}".format(c.get_out()[-1]))

import sys
import os
from itertools import permutations

sys.path.append('../')
import intcode

file_name = ''

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    # If no file provided, try to find 'input' in script folder
    path = os.path.realpath(__file__).rsplit('/',1)[0]
    file_name = path+'/input'

init_prog = [int(x) for x in open(file_name).read().split(',')]

print("Part 1: {}".format(intcode.run(init_prog[:], [1])[0]))
print("Part 2: {}".format(intcode.run(init_prog[:], [2])[0]))

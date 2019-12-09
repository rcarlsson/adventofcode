import sys
import os
import operator

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

program = [init_prog[0], 12, 2] + init_prog[3:]
intcode.run(program)
print("Part 1: {}".format(program[0]))

for x in range(100):
    for y in range(100):
        program = [init_prog[0], x, y] + init_prog[3:]
        intcode.run(program)
        if (program[0] == 19690720):
            print("Part 2: {}".format(100*x + y))
            exit(0) 

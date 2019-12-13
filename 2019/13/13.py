import sys
import os

sys.path.append('../')
from intcode import *

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

program = [int(x) for x in open(file_name).read().split(',')]

c = IntCode(program)
while c.run() != Result.HALT: {}
print("Part 1: {}".format(c.get_out()[2::3].count(2)))

c = IntCode([2] + program[1:])
grid = {}
score = 0

def get_state(grid):
    for key in grid.keys():
        if grid[key] == 3:
            paddle = key
        if grid[key] == 4:
            ball = key
    return paddle,ball

while True:
    res = c.run()
    if res == Result.INPUT:
        p,b = get_state(grid)
        c.give_inp(int(b.real-p.real))
    elif res == Result.OUTPUT:
        c.run()
        c.run()
        (x,y,z) = c.get_out()
        if x+y*1j == -1:
            score = z
        else:
            grid[x+y*1j] = z
        c.out = []
    elif res == Result.HALT:
        print("Part 2: {}".format(score))
        break
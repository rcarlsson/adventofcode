import sys
import os

sys.path.append('../')
from intcode import *

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

program = [int(x) for x in open(file_name).read().split(',')]

def bot(prog, panels):
    pos = 0
    direction = -1j
    c = IntCode(prog)
    while True:
        c.give_inp(panels.get(pos,0))
        if c.run() == Result.HALT: return panels
        panels[pos] = c.get_out()[-1]
        if c.run() == Result.HALT: return panels
        direction *= 1j if c.get_out()[-1] == 1 else -1j
        pos += direction

print("Part 1: {}".format(len(bot(program,{}))))

panels = bot(program,{0: 1})
xl,yl = zip(*[(int(c.real),int(c.imag)) for c in panels])
print("Part 2:")
for y in range(min(yl),max(yl)+1):
    print(''.join(['#' if panels.get(x+y*1j, 0) == 1 else ' ' for x in range(min(xl),max(xl)+1)]))

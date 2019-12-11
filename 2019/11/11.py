import sys
import os

sys.path.append('../')
import intcode

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

init_prog = [int(x) for x in open(file_name).read().split(',')]

def bot(prog, panels={}):
    pos = 0
    direction = -1j
    ip = 0
    rel_ptr = 0
    state = 0 # 0=paint, 1=turn and move
    while True:
        (out, ip, rel_ptr) = intcode.run(prog, [panels.get(pos, 0)], ip, rel_ptr)
        if out is None:
            return panels
        elif state == 0:
            panels[pos] = out
            state = 1
        else:
            direction *= 1j if out == 1 else -1j
            pos += direction
            state = 0

print("Part 1: {}".format(len(bot(init_prog[:]))))

panels = bot(init_prog[:],{0: 1})
xl = [int(c.real) for c in panels.keys()]
yl = [int(c.imag) for c in panels.keys()]
print("Part 2:")
for y in range(min(yl),max(yl)+1):
    print(''.join(['#' if panels.get(x+y*1j, 0) == 1 else ' ' for x in range(min(xl),max(xl)+1)]))

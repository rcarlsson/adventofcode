import sys
import os

sys.path.append('../')
import intcode

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

init_prog = [int(x) for x in open(file_name).read().split(',')]

def get_last_out(program, inp):
    ip = 0
    out = 0
    while True:
        (res, ip, _) = intcode.run(program, [inp], ip)
        if res is None:
            return out
        else:
            out = res

print("Part 1: {}".format(get_last_out(init_prog[:], 1)))
print("Part 2: {}".format(get_last_out(init_prog[:], 5)))

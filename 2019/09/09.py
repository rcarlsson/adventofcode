import sys
import os
from itertools import permutations

file_name = ''

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    # If no file provided, try to find 'input' in script folder
    path = os.path.realpath(__file__).rsplit('/',1)[0]
    file_name = path+'/input'

init_prog = [int(x) for x in open(file_name).read().split(',')]

def execute(program, ip, inp):
    out = None
    rel_ptr = 0
    while program[ip] != 99 and ip >= 0 and ip < len(program):
        op = program[ip] % 100
        m1 = (program[ip] // 100) % 10
        m2 = (program[ip] // 1000) % 10
        m3 = (program[ip] // 10000) % 10

        if m1 == 0:
            p1 = program[ip+1]
        elif m1 == 1:
            p1 = ip+1
        elif m1 == 2:
            p1 = program[ip+1]+rel_ptr

        if m2 == 0:
            p2 = program[ip+2]
        elif m2 == 1:
            p2 = ip+2
        elif m2 == 2:
            p2 = program[ip+2]+rel_ptr

        if m3 == 0:
            p3 = program[ip+3]
        elif m3 == 1:
            p3 = ip+3
        elif m3 == 2:
            p3 = program[ip+3]+rel_ptr

        if op == 1:
            program[p3] = program[p1] + program[p2]
            ip += 4
        elif op == 2:
            program[p3] = program[p1] * program[p2]
            ip += 4
        elif op == 3:
            program[p1] = inp.pop(0)
            ip += 2
        elif op == 4:
            ip += 2
            out = program[p1]
            break
        elif op == 5:
            ip = program[p2] if program[p1] != 0 else ip+3
        elif op == 6:
            ip = program[p2] if program[p1] == 0 else ip+3
        elif op == 7:
            program[p3] = 1 if program[p1] < program[p2] else 0
            ip += 4
        elif op == 8:
            program[p3] = 1 if program[p1] == program[p2] else 0
            ip += 4
        elif op == 9:
            rel_ptr += program[p1]
            ip += 2

    return (program, ip, inp, out)

prog = init_prog[:] + [0 for _ in range(100)]
(_, _, _, res1) = execute(prog, 0, [1])
print("Part 1: {}".format(res1))

prog = init_prog[:] + [0 for _ in range(10000)]
(_, _, _, res2) = execute(prog, 0, [2])
print("Part 2: {}".format(res2))

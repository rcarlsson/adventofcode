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
    while program[ip] != 99 and ip >= 0 and ip < len(program):
        op = program[ip] % 100
        m1 = (program[ip] // 100) % 10
        m2 = (program[ip] // 1000) % 10
        m3 = (program[ip] // 10000) % 10

        p1 = ip+1 if m1 == 1 else program[ip+1]
        p2 = ip+2 if m2 == 1 else program[ip+2]
        if ip+3 < len(program):
            p3 = ip+3 if m3 == 1 else program[ip+3]

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
            return (program, ip, inp, program[p1])
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

    return (program, ip, inp, None)

res1 = 0
for p in permutations([0,1,2,3,4]):
    res = 0
    prog = [init_prog[:] for _ in range(5)]
    for i in range(5):
        (_, _, _, res) = execute(prog[i], 0, [p[i], res])

    res1 = max(res1, res)

print("Part 1: {}".format(res1))

res2 = 0
for p in permutations([5,6,7,8,9]):
    res = 0
    tmp_res = 0
    prog = [init_prog[:] for _ in range(5)]
    ip = [0 for _ in range(5)]
    inp = [[p[i]] for i in range(5)]
    while tmp_res is not None:
        for i in range(5):
            inp[i].append(res)
            (prog[i], ip[i], inp[i], tmp_res) = execute(prog[i], ip[i], inp[i])
            res = res if tmp_res is None else tmp_res
    res2 = max(res2, res)

print("Part 2: {}".format(res2))

import sys
import os
import operator
import math

file_name = ''

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    # If no file provided, try to find 'input' in script folder
    path = os.path.realpath(__file__).rsplit('/',1)[0]
    file_name = path+'/input'

init_prog = [int(x) for x in open(file_name).read().split(',')]

def execute(program, id):
    ip = 0
    res = 0
    while program[ip] != 99 and ip >= 0 and ip < len(program):
        op = program[ip] % 100
        m1 = (program[ip] // 100) % 10
        m2 = (program[ip] // 1000) % 10
        m3 = (program[ip] // 10000) % 10

        p1 = ip+1 if m1 == 1 else program[ip+1]
        p2 = ip+2 if m2 == 1 else program[ip+2]
        p3 = ip+3 if m3 == 1 else program[ip+3]

        if op == 1:
            program[p3] = program[p1] + program[p2]
            ip += 4
        elif op == 2:
            program[p3] = program[p1] * program[p2]
            ip += 4
        elif op == 3:
            program[p1] = id
            ip += 2
        elif op == 4:
            res = program[p1]
            ip += 2
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

    return res

program = init_prog[:]
print("Part 1: {}".format(execute(program, 1)))
program = init_prog[:]
print("Part 2: {}".format(execute(program, 5)))

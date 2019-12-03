import sys
import operator

file_name = sys.argv[1]

init_prog = [int(x) for x in open(file_name).read().split(',')]

oper = {}
oper[1] = operator.add
oper[2] = operator.mul

def execute(program):
    ip = 0
    while program[ip] != 99 and ip >= 0 and ip < len(program):
        opcode = program[ip]
        (a1, a2, a3) = program[ip+1 : ip+4]
        program[a3] = oper[opcode](program[a1], program[a2])
        ip += 4

    return program[0]

program = init_prog[:]
program[1] = 12
program[2] = 2
print("Part 1: {}".format(execute(program)))

noun = 0
verb = 0
for x in range(100):
    for y in range(100):
        program = init_prog[:]
        program[1] = x
        program[2] = y
        if (execute(program) == 19690720):
            noun = x
            verb = y
            break

print("Part 2: {}".format(100*noun + verb))

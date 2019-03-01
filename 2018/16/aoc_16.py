import sys
import re


def execute(opcode, a, b, c, reg):
    r = reg.copy()
    if opcode == 'addr':
        r[c] = r[a] + r[b]
    elif opcode == 'addi':
        r[c] = r[a] + b
    elif opcode == 'mulr':
        r[c] = r[a] * r[b]
    elif opcode == 'muli':
        r[c] = r[a] * b
    elif opcode == 'banr':
        r[c] = r[a] & r[b]
    elif opcode == 'bani':
        r[c] = r[a] & b
    elif opcode == 'borr':
        r[c] = r[a] | r[b]
    elif opcode == 'bori':
        r[c] = r[a] | b
    elif opcode == 'setr':
        r[c] = r[a]
    elif opcode == 'seti':
        r[c] = a
    elif opcode == 'gitr':
        r[c] = (a > r[b])
    elif opcode == 'gtri':
        r[c] = (r[a] > b)
    elif opcode == 'gtrr':
        r[c] = (r[a] > r[b])
    elif opcode == 'eqir':
        r[c] = (a == r[b])
    elif opcode == 'eqri':
        r[c] = (r[a] == b)
    elif opcode == 'eqrr':
        r[c] = (r[a] == r[b])

    return r


opcodes = {'addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gitr', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr'}

opcode_map = []
for i in range(16):
    opcode_map.append(opcodes.copy())

def test_input(op, a, b, c, before, after):
    matches = 0
    for opcode in opcodes:
        if execute(opcode, a, b, c, before) == after:
            matches += 1
        elif opcode in opcode_map[op]:
            opcode_map[op].remove(opcode)
    return matches


input = sys.stdin.read().rstrip().split('\n')

result = 0
before = [0,0,0,0]
after = [0,0,0,0]
a = 0
b = 0
c = 0
for line in input:
    if line.startswith('Before'):
        before = list(map(int, re.findall(r'\d+', line)))
    elif line.startswith('After'):
        after = list(map(int, re.findall(r'\d+', line)))
        if test_input(op, a, b, c, before, after) >= 3:
            result += 1
    elif line != '':
        op,a,b,c = map(int, line.split())

print('Part 1: {0}'.format(result))

for _ in range(16):
    for i, op in enumerate(opcode_map):
        if len(op) == 1:
            for j, _ in enumerate(opcode_map):
                for o in op:
                    if j != i and o in opcode_map[j]:
                        opcode_map[j].remove(o)

for i, op in enumerate(opcode_map):
    opcode_map[i] = list(opcode_map[i])[0]

reg = [0,0,0,0]
sample = True
for line in input:
    if line.startswith('Before'):
        sample = True
    elif line.startswith('After'):
        sample = False
    elif line != '' and sample == False:
        op,a,b,c = map(int, line.split())
        reg = execute(opcode_map[op], a, b, c, reg)

print('Part 2: {0}'.format(reg[0]))








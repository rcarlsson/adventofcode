import sys
import re


def execute(opcode, a, b, c, r):
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


input = sys.stdin.read().rstrip().split('\n')
ip_reg = int(re.findall(r'\d+', input[0])[0])
instr = []
for line in input[1:]:
    i,a,b,c = line.split()
    a = int(a)
    b = int(b)
    c = int(c)
    instr.append([i,a,b,c])

regs = [0,0,0,0,0,0]
"""while regs[ip_reg] >= 0 and regs[ip_reg] < len(instr):
    i = instr[regs[ip_reg]]
    execute(i[0], i[1], i[2], i[3], regs)
    regs[ip_reg] += 1"""

regs[3] = 4*19*11 + 8*22 + 13
regs[1] = 1
while regs[1] <= regs[3]:
    if regs[3] % regs[1] == 0:
        regs[0] += regs[1]
    regs[1] += 1
print('Part 1: {0}'.format(regs[0]))

regs[3] += (27*28+29)*30*14*32
regs[0] = 0
regs[1] = 1
while regs[1] <= regs[3]:
    if regs[3] % regs[1] == 0:
        regs[0] += regs[1]
    regs[1] += 1

print('Part 2: {0}'.format(regs[0]))








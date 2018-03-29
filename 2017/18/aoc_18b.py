import sys
import string
from collections import deque


queue = [deque(), deque()]
p1_snd_count = 0


def execute_line(line, program_id, registers):
    global queue
    global p1_snd_count

    result = 0

    oper, reg, *params = line.split()

    val = 0

    if params:
        try:
            val = int(params[0])
        except ValueError:
            val = registers[params[0]]

    if oper == 'snd':
        try:
            val = int(reg)
        except ValueError:
            val = registers[reg]

        queue[(program_id+1) % 2].append(val)
        if program_id == 1:
            p1_snd_count += 1

    elif oper == 'set':
        registers[reg] = val

    elif oper == 'add':
        registers[reg] += val

    elif oper == 'mul':
        registers[reg] *= val

    elif oper == 'mod':
        registers[reg] %= val

    elif oper == 'rcv':
        if queue[program_id]:
            registers[reg] = queue[program_id].popleft()
        else:
            result = -1000000

    elif oper == 'jgz':
        try:
            condition = int(reg)
        except ValueError:
            condition = registers[reg]
        if condition > 0:
            result = val - 1

    return result


def solve(file_name):
    registers = [dict.fromkeys(string.ascii_lowercase[0:16], 0), dict.fromkeys(string.ascii_lowercase[0:16], 0)]
    registers[1]['p'] = 1
    address = [0, 0]
    paused = [False, False]
    terminated = [False, False]
    commands = []
    running_program = 0

    with open(file_name) as f:
        for line in f:
            commands.append(line)

    while True:
        result = execute_line(commands[address[running_program]], running_program, registers[running_program])

        if result == -1000000:  # rcv but nothing in queue
            paused[running_program] = True
            running_program = (running_program + 1) % 2

        else:
            address[running_program] = address[running_program] + result + 1

            if address[running_program] not in range(len(commands)):
                terminated[running_program] = True
                running_program = (running_program + 1) % 2
            else:
                paused[0] = paused[1] = False

        if (terminated[0] or paused[0]) and (terminated[1] or paused[1]):
            break

    return p1_snd_count


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

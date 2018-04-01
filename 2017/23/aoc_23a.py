import sys
import string


mul_count = 0


def execute_line(line, registers, address):
    global mul_count

    oper, reg, *params = line.split()

    val = 0

    if params:
        try:
            val = int(params[0])
        except ValueError:
            val = registers[params[0]]

    if oper == 'set':
        registers[reg] = val

    elif oper == 'sub':
        registers[reg] -= val

    elif oper == 'mul':
        registers[reg] *= val
        mul_count += 1

    elif oper == 'jnz':
        try:
            condition = int(reg)
        except ValueError:
            condition = registers[reg]
        if condition != 0:
            address += val - 1

    return address


def solve(file_name):
    registers = dict.fromkeys(string.ascii_lowercase[0:8], 0)
    address = 0
    commands = []

    with open(file_name) as f:
        for line in f:
            commands.append(line)

    while address in range(len(commands)):
        address = execute_line(commands[address], registers, address)
        address += 1

    return mul_count


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

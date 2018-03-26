import sys


def solve(f):
    registers = dict()
    instructions = []

    for line in f:
        instruction = line.split()
        name = instruction[0]
        registers[name] = 0
            
        operator_str = instruction[1]
        if operator_str == 'dec':
            operator = '-='
        else:
            operator = '+='

        parameter = instruction[2]
        condition = instruction[3:]
        condition[1] = 'registers[\''+condition[1]+'\']'
        name = 'registers[\''+name+'\']'

        instructions.append(' '.join(condition) + ': ' + name + operator + parameter)

    for x in instructions:
        exec(x)

    v = list(registers.values())
    return v[v.index(max(v))]


def main():
    file_name = sys.argv[1]
    with open(file_name) as f:
        output = solve(f)
        print('{0}'.format(output))


if __name__ == "__main__":
    main()

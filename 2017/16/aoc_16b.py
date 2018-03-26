import sys


def execute_commands(commands, program_string):

    programs = list(program_string)

    for command in commands:
        if command[0] == 's':
            shift = int(command[1:])
            programs = programs[-shift:] + programs[:-shift]
        elif command[0] == 'x':
            pos = command[1:].split('/')
            a = int(pos[0])
            b = int(pos[1])
            tmp = programs[a]
            programs[a] = programs[b]
            programs[b] = tmp
        elif command[0] == 'p':
            progs = command[1:].split('/')
            a = programs.index(progs[0])
            b = programs.index(progs[1])
            tmp = programs[a]
            programs[a] = programs[b]
            programs[b] = tmp

    return ''.join(programs)


def solve(file_name):

    programs = 'abcdefghijklmnop'

    with open(file_name) as f:
        for line in f:
            commands = line.split(',')

            transformed_programs = execute_commands(commands, programs)

            for i in range(1, 1000000000):
                transformed_programs = execute_commands(commands, transformed_programs)
                if transformed_programs == programs:
                    for i in range(1000000000%(i+1)):
                        transformed_programs = execute_commands(commands, transformed_programs)

                    return transformed_programs

            return transformed_programs


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

import sys


accessible_programs_set = set()

def fillin_accessible_programs(program_list, program_id):

    for program in program_list[program_id]:
        if program not in accessible_programs_set:
            accessible_programs_set.add(program)
            fillin_accessible_programs(program_list, program)


def solve(file_name):

    program_list = []
    group_count = 0

    with open(file_name) as f:
        for line in f:
            line = line.replace("<-> ", "")
            line = line.replace(",", "")
            program_list.append(list(map(int, line.split())))

    for part in program_list:
        if part[0] not in accessible_programs_set:
            fillin_accessible_programs(program_list, part[0])
            group_count += 1

    return group_count


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

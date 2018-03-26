import sys


def solve_line(line):
    return line


def solve(file_name):
    with open(file_name) as f:
        for line in f:
            line_result = solve_line(line)
            print('{0}'.format(line_result))
    return file_name


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

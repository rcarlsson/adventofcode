import sys


def add_line(line):
    return int(line)


def solve(file_name):
    with open(file_name) as f:
        result = 0
        for line in f:
            result += add_line(line)
    return result


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

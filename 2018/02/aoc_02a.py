import sys
from string import ascii_lowercase


def solve_line(line):
    twos = 0
    threes = 0
    for c in ascii_lowercase :
        if line.count(c) == 2:
            twos = 1
        elif line.count(c) == 3:
            threes = 1
        if twos == 1 and threes == 1:
            break

    return (twos, threes)


def solve(file_name):
    with open(file_name) as f:
        twos = 0
        threes = 0
        tmp2 = 0
        tmp3 = 0
        for line in f:
            (tmp2, tmp3) = solve_line(line)
            twos = twos + tmp2
            threes = threes + tmp3
    return twos*threes


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

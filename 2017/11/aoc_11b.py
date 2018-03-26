import sys


def solve_line(line):
    movements = line.split(',')
    x = 0
    y = 0
    max_distance = 0

    for movement in movements:
        if movement == 'n':
            y += 1
        elif movement == 'ne':
            y += 0.5
            x += 0.5
        elif movement == 'se':
            y -= 0.5
            x += 0.5
        elif movement == 's':
            y -= 1
        elif movement == 'sw':
            y -= 0.5
            x -= 0.5
        elif movement == 'nw':
            y += 0.5
            x -= 0.5

        max_distance = max(max_distance, abs(x)+abs(y))

    return int(max_distance)


def solve(file_name):
    with open(file_name) as f:
        for line in f:
            line_result = solve_line(line)
            print('{0}'.format(line_result))
    return file_name


def main():
    file_name = sys.argv[1]
    result = solve(file_name)


if __name__ == "__main__":
    main()

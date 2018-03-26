import sys


def solve_line(line):
    movements = line.split(',')
    n = movements.count('n')
    ne = movements.count('ne')
    se = movements.count('se')
    s = movements.count('s')
    sw = movements.count('sw')
    nw = movements.count('nw')

    movement_y = abs(n-s + (ne+nw-se-sw)/2)
    movement_x = abs(ne+se-nw-sw)/2

    result = int(movement_x + movement_y)
    return result


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

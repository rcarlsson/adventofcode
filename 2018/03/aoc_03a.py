import sys
import re

data_size = 1000
claims = [[0]*data_size for i in range(data_size)]

def solve_line(line):
    global claims

    input = re.split('#| @ |,|: |x|\n', line)
    x_start = int(input[2])
    y_start = int(input[3])
    x_size = int(input[4])
    y_size = int(input[5])

    for x in range(x_start,x_start+x_size):
        for y in range(y_start,y_start+y_size):
            claims[x][y] = claims[x][y]+1

    return line


def solve(file_name):
    with open(file_name) as f:
        for line in f:
            line_result = solve_line(line)
    
    result = 0
    for x in range(data_size):
        for y in range(data_size):
            if claims[x][y] > 1:
                result = result + 1
    return result


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

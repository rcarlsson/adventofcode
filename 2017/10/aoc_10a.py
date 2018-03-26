import sys


def solve_line(string_length, line):
    lengths = list(map(int, line.split(',')))
    idx = 0
    skip_length = 0
    string_list = list(range(string_length))

    for value in lengths:
        if idx+value > string_length:
            sub_string = string_list[idx:] + string_list[:idx+value-string_length]
            sub_string.reverse()
            string_list[idx:] = sub_string[:string_length-idx]
            string_list[0:idx+value-string_length] = sub_string[string_length-idx:]
        else:
            sub_string = string_list[idx:idx+value]
            sub_string.reverse()
            string_list[idx:idx+value] = sub_string

        idx = (idx+value+skip_length) % string_length
        skip_length += 1

    return string_list[0]*string_list[1]


def solve(file_name):
    with open(file_name) as f:
        for line in f:
            line_result = solve_line(256, line)
            return line_result


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

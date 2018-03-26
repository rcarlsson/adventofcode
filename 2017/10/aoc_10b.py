import sys
from functools import reduce


def solve_line(string_length, line):

    lengths = []
    idx = 0
    skip_length = 0
    string_list = list(range(string_length))
    result = []
    result_string = ""

    # convert to ascii
    for char in line:
        lengths.append(ord(char))

    # add sequence
    lengths += [17, 31, 73, 47, 23]

    # run 64 times
    for i in range(64):
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


    # bitwise XOR 16 numbers at a time -> 16 new numbers
    for i in range(16):
        result.append(reduce((lambda x, y: x ^ y), string_list[i*16:(i+1)*16]))

        # print hexadecimal representation
        result_string += '{:02x}'.format(result[i])

    return result_string


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

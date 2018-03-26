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

    return result


def clear_group(data, row, col):

    data[row][col] = 0

    if row < len(data)-1 and data[row+1][col] == 1:
        data = clear_group(data, row+1, col)

    if row > 0 and data[row-1][col] == 1:
        data = clear_group(data, row-1, col)

    if col < len(data[row])-1 and data[row][col+1] == 1:
        data = clear_group(data, row, col+1)

    if col > 0 and data[row][col-1] == 1:
        data = clear_group(data, row, col-1)

    return data


def calc_groups(data):

    groups = 0

    for row_idx in range(len(data)):

        for col_idx in range(len(data[row_idx])):

            if data[row_idx][col_idx] == 1:
                clear_group(data, row_idx, col_idx)
                groups += 1

    return groups

def solve(input_string):
    result = []
    for row in range(128):
        line_result = solve_line(256, input_string+"-"+str(row))
        result_string = ""
        for n in line_result:
            result_string += '{0:08b}'.format(n)

        result.append(list(map(int, result_string)))

    groups = calc_groups(result)

    return groups


def main():
    result = solve("stpzcrnm")
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

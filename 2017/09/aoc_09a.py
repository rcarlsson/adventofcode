import sys


def solve(data_stream):
    garbage = False
    negate = False
    value = 0
    result = 0
    for idx in range(len(data_stream)):
        char = data_stream[idx]

        if negate:
            negate = False
        elif char == "!":
            negate = True
        elif char == "<":
            garbage = True
        elif char == ">":
            garbage = False
        elif not garbage and char == "{":
            value += 1
        elif not garbage and char == "}":
            result += value
            value -= 1
    return result


def main():
    file_name = sys.argv[1]
    with open(file_name) as f:
        for line in f:
            data_stream = line
            output = solve(data_stream)
            print('{0}'.format(output))


if __name__ == "__main__":
    main()

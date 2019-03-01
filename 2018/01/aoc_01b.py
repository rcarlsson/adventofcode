import sys

result = 0
results = [0]

def add_line(line):
    return int(line)


def solve(file_name):
    global result
    global results

    with open(file_name) as f:
        for line in f:
            result += add_line(line)
            if result in results:
                return result
            results.append(result)
    return -99999999


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    while result == -99999999:
        # This takes ~30s...
        result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

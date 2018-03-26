import sys


def solve(file_name):

    nr_of_layers = 95
    scanner_list = [0] * nr_of_layers
    severity = 0

    with open(file_name) as f:
        for line in f:
            scanner = list(map(int, line.replace(":", "").split()))
            scanner_list[scanner[0]] = scanner[1]

    for layer in range(nr_of_layers):
        scanner_range = scanner_list[layer]

        if scanner_range != 0 and layer % (scanner_range*2-2) == 0:
            severity += scanner_range * layer

    return severity


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

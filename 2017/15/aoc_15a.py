

factor_a = 16807
factor_b = 48271
divisor = 2147483647


def solve(start_a, start_b, iterations):

    a = start_a
    b = start_b
    matches = 0

    for i in range(iterations):
        a = (a * factor_a) % divisor
        b = (b * factor_b) % divisor
        if (a & 0xffff) == (b & 0xffff):
            matches += 1

    return matches


def main():
    start_a = 699
    start_b = 124
    iterations = 40000000
    result = solve(start_a, start_b, iterations)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

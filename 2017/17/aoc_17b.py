

def solve(step_size, iterations):

    idx = 0
    result = 0

    for i in range(iterations):
        idx = (idx+step_size) % (i+1)
        if idx == 0:
            result = i+1

        idx += 1

    return result


def main():
    result = solve(335, 50000000)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

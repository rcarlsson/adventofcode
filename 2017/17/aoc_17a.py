

def solve(step_size, iterations):

    idx = 0
    buffer = [0]

    for i in range(iterations):
        idx = (idx+step_size) % len(buffer)
        buffer.insert(idx+1, i+1)
        idx += 1

    return buffer[idx+1]


def main():
    result = solve(335, 2017)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

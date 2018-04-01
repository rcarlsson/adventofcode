import sys


def create_bridge(used_components, port, components):
    strongest_bridge = 0
    done = True

    for idx in range(len(components)):

        if idx not in used_components and port in components[idx]:
            strongest_bridge = max(create_bridge(used_components + [idx], components[idx][(components[idx].index(port) + 1) % 2], components), strongest_bridge)
            done = False

    if done:
        for idx in used_components:
            strongest_bridge += sum(components[idx])
            print('{0}'.format(strongest_bridge))

    return strongest_bridge


def solve(file_name):
    components = []
    strongest_bridge = 0

    with open(file_name) as f:
        for line in f:
            components.append(list(map(int, line.split('/'))))

    for idx in range(len(components)):
        if 0 in components[idx]:
            port = components[idx][(components[idx].index(0) + 1) % 2]
            used_components = [idx]
            strongest_bridge = max(create_bridge(used_components, port, components), strongest_bridge)

    return strongest_bridge


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

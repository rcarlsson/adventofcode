import sys


best_bridge = {'strength': 0, 'length': 0}


def create_bridge(used_components, port, components):
    global best_bridge
    strength = 0
    done = True

    for idx in range(len(components)):

        if idx not in used_components and port in components[idx]:
            create_bridge(used_components + [idx], components[idx][(components[idx].index(port) + 1) % 2], components)
            done = False

    if done:
        length = len(used_components)

        if length >= best_bridge['length']:
            for idx in used_components:
                strength += sum(components[idx])
            if strength > best_bridge['strength'] or length > best_bridge['length']:
                best_bridge['strength'] = strength
                best_bridge['length'] = length

    return


def solve(file_name):
    components = []

    with open(file_name) as f:
        for line in f:
            components.append(list(map(int, line.split('/'))))

    for idx in range(len(components)):
        if 0 in components[idx]:
            port = components[idx][(components[idx].index(0) + 1) % 2]
            used_components = [idx]
            create_bridge(used_components, port, components)

    return best_bridge['strength']


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

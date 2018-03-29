import sys


steps = 0


def change_dir(direction, x, y, graph):
    if direction == 'u' or direction == 'd':
        if graph[y][x+1] == '-':
            return 'r'
        else:
            return 'l'
    else:
        if graph[y+1][x] == '|':
            return 'd'
        else:
            return 'u'


def move(direction, x, y):
    global steps

    steps += 1

    if direction == 'u':
        return x, y-1
    elif direction == 'd':
        return x, y+1
    elif direction == 'l':
        return x-1, y
    else:
        return x+1, y


def solve(file_name):
    global steps

    graph = []
    direction = 'd'
    result = []
    with open(file_name) as f:
        for line in f:
            graph.append(line)

    x = graph[0].find('|')
    y = 0

    while graph[y][x] != ' ':
        if graph[y][x] == '+':
            direction = change_dir(direction, x, y, graph)
            x, y = move(direction, x, y)
        elif graph[y][x] == '-' or graph[y][x] == '|':
            x, y = move(direction, x, y)
        else:
            result.append(graph[y][x])
            x, y = move(direction, x, y)

    return steps


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

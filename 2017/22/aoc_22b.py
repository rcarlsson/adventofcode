import sys


infections_caused = 0


def action(direction, x, y, grid):
    global infections_caused

# 0 = clean
# 1 = weakened
# 2 = infected
# 3 = flagged
    if grid[y][x] == 0:
        direction = (direction-1) % 4
    elif grid[y][x] == 1:
        infections_caused += 1
    elif grid[y][x] == 2:
        direction = (direction+1) % 4
    else:
        direction = (direction+2) % 4

    grid[y][x] = (grid[y][x]+1) % 4

    if direction == 0:
        y -= 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y += 1
    else:
        x -= 1

    return direction, x, y, grid


def solve(file_name, iterations):
    global infections_caused
    direction = 0
    grid = []
    infections_caused = 0

    with open(file_name) as f:
        for line in f:
            line = line.replace('#', '2')
            line = line.replace('.', '0')
            grid.append(list(map(int, list(line[:-1]))))

    x = int(len(grid)/2)
    y = int(len(grid)/2)

    for i in range(iterations):
        direction, x, y, grid = action(direction, x, y, grid)

        if x < 0:
            for idx in range(len(grid)):
                grid[idx].insert(0, 0)
            x += 1

        if x >= len(grid[0]):
            for idx in range(len(grid)):
                grid[idx].append(0)

        if y < 0:
            grid.insert(0, [0]*len(grid[0]))
            y += 1

        if y >= len(grid):
            grid.append([0]*len(grid[0]))

    return infections_caused


def main():
    file_name = sys.argv[1]
    iterations = int(sys.argv[2])
    result = solve(file_name, iterations)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

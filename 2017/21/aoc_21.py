import sys


def rotate_grid(grid):

    if len(grid) == 2:
        return [grid[1][0]+grid[0][0], grid[1][1]+grid[0][1]]
    else:
        return [grid[2][0]+grid[1][0]+grid[0][0], grid[2][1]+grid[1][1]+grid[0][1], grid[2][2]+grid[1][2]+grid[0][2]]


def flip_grid(grid):

    result = []

    for row in grid:
        result.append(row[::-1])

    return result


def get_all_variations(grid):
    grids = list()
    grids.append(grid)
    grids.append(rotate_grid(grids[0]))
    grids.append(rotate_grid(grids[1]))
    grids.append(rotate_grid(grids[2]))
    grids.append(flip_grid(grids[0]))
    grids.append(rotate_grid(grids[4]))
    grids.append(rotate_grid(grids[5]))
    grids.append(rotate_grid(grids[6]))

    return grids


def convert_grid(grid, before, after):
    grids = get_all_variations(grid)

    for entry in grids:
        try:
            return after[before.index(entry)]
        except ValueError:
            continue


def expand_grid(grid):
    size = len(grid)

    if size % 2 == 0:
        mod = 2
        before = before_2
        after = after_2
    else:
        mod = 3
        before = before_3
        after = after_3

    new_grid = ['']*int(size+size/mod)

    for row in range(0, size, mod):
        for col in range(0, size, mod):
            tmp_grid = []
            for i in range(mod):
                tmp_grid.append(grid[row+i][col:col+mod])

            tmp_grid = convert_grid(tmp_grid, before, after)

            for i in range(mod+1):
                new_grid[int(row/mod)*(mod+1)+i] += tmp_grid[i]
    return new_grid


before_2 = []
before_3 = []
after_2 = []
after_3 = []


def solve(file_name, iterations):

    global before_2
    global before_3
    global after_2
    global after_3
    grid = ['.#.', '..#', '###']

    with open(file_name) as f:
        for line in f:
            b, a = line.split(' => ')

            if len(b) == 5:
                before_2.append(b.split('/'))
                after_2.append(a.strip().split('/'))
            else:
                before_3.append(b.split('/'))
                after_3.append(a.strip().split('/'))

    for i in range(iterations):
        grid = expand_grid(grid)

    count = 0
    for row in grid:
        count += row.count('#')

    return count


def main():
    file_name = sys.argv[1]
    iterations = int(sys.argv[2])
    result = solve(file_name, iterations)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

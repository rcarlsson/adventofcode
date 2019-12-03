import sys

file_name = sys.argv[1]

paths = [line.rstrip('\n').split(',') for line in open(file_name)]

dirs = {}
dirs['R'] = (1,0)
dirs['L'] = (-1,0)
dirs['U'] = (0,1)
dirs['D'] = (0,-1)

def generate_grid(moves):
    grid = set()
    curr_pos = (0,0)
    for move in moves:
        dir = dirs[move[0]]
        dist = int(move[1:])

        for _ in range(dist):
            curr_pos = (curr_pos[0]+dir[0], curr_pos[1]+dir[1])
            grid.add(curr_pos)

    return grid

def calc_dist(moves, goal):
    tot_dist = 0
    curr_pos = (0,0)
    for move in moves:
        dir = dirs[move[0]]
        dist = int(move[1:])

        for _ in range(dist):
            tot_dist += 1
            curr_pos = (curr_pos[0]+dir[0], curr_pos[1]+dir[1])
            if curr_pos == goal:
                return tot_dist

    return sys.maxsize

intersections = generate_grid(paths[0]).intersection(generate_grid(paths[1]))

res1 = min(abs(x)+abs(y) for (x,y) in intersections)
print("Part 1: {}".format(res1))

res2 = min(calc_dist(paths[0], pos) + calc_dist(paths[1], pos) for pos in intersections)
print("Part 2: {}".format(res2))
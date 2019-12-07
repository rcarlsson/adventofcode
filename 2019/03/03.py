import sys
import os

file_name = ''

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    # If no file provided, try to find 'input' in script folder
    path = os.path.realpath(__file__).rsplit('/',1)[0]
    file_name = path+'/input'

paths = [line.rstrip('\n').split(',') for line in open(file_name)]

dirs = {}
dirs['R'] = (1,0)
dirs['L'] = (-1,0)
dirs['U'] = (0,1)
dirs['D'] = (0,-1)

def generate_grid(moves):
    grid = {}
    d = 0
    curr_pos = (0,0)
    for move in moves:
        dir = dirs[move[0]]
        dist = int(move[1:])

        for _ in range(dist):
            curr_pos = (curr_pos[0]+dir[0], curr_pos[1]+dir[1])
            d += 1
            grid[curr_pos] = d

    return grid

p1 = generate_grid(paths[0])
p2 = generate_grid(paths[1])
intersections = p1.keys() & p2.keys()

res1 = min(abs(x)+abs(y) for (x,y) in intersections)
print("Part 1: {}".format(res1))

res2 = min(p1[pos] + p2[pos] for pos in intersections)
print("Part 2: {}".format(res2))
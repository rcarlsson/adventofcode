import sys
import os

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

paths = [line.rstrip('\n').split(',') for line in open(file_name)]

dirs = {'R': 1, 'L': -1, 'U': -1j, 'D': 1j}

def generate_grid(moves):
    grid = {}
    d = 0
    pos = 0
    for move in moves:
        for _ in range(int(move[1:])):
            pos += dirs[move[0]]
            d += 1
            grid[pos] = d

    return grid

p1 = generate_grid(paths[0])
p2 = generate_grid(paths[1])
intersections = p1.keys() & p2.keys()

print("Part 1: {}".format(int(min(abs(pos.real)+abs(pos.imag) for pos in intersections))))

print("Part 2: {}".format(min(p1[pos] + p2[pos] for pos in intersections)))
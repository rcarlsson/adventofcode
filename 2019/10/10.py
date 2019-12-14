import sys
import os
from fractions import gcd
import numpy as np

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

lines = [line.rstrip('\n') for line in open(file_name)]
height = len(lines)
width = len(lines[0])
asteroids = set()
for y in range(height):
    for x in range(width):
        if lines[y][x] == '#':
            asteroids.add((x,y))

def get_visible(base, asteroids):
    visible = asteroids.copy()
    visible.discard(base)
    for a in asteroids:
        if a == base:
            continue
        xd = a[0]-base[0]
        yd = a[1]-base[1]
        divisor = abs(gcd(xd,yd))
        xd = xd/divisor
        yd = yd/divisor
        xn = a[0]+xd
        yn = a[1]+yd
        while xn >= 0 and xn < width and yn >= 0 and yn < height:
            visible.discard((xn,yn))
            xn += xd
            yn += yd

    return visible

res1 = 0
base = None
for a in asteroids:
        tmp = len(get_visible(a, asteroids))
        if tmp > res1:
            res1 = tmp
            base = a

print("Part 1: {}".format(res1))

angles = {}
asteroids.remove(base)
for asteroid in asteroids:
    angle = np.pi - np.arctan2(asteroid[0]-base[0], asteroid[1]-base[1])
    if angle in angles:
        angles[angle].append(asteroid)
        angles[angle].sort(key=lambda ast: abs(ast[0]-base[0])+abs(ast[1]-base[1]))
    else:
        angles[angle] = [asteroid]

rm_count = 0
while angles:
    for angle in sorted(angles):
        if angles[angle]:
            asteroid = angles[angle].pop(0)
            rm_count += 1
        else:
            del(angles[angle])

        if rm_count == 200:
            print("Part 2: {}".format(asteroid[0]*100 + asteroid[1]))
            exit(0)

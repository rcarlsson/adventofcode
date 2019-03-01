import sys
from itertools import product


s = sys.stdin.read().rstrip().split('\n')


max_size = 400

# Starting coords
s_c = set()
for i in s:
    s_c.add(tuple(map(int, (i.split(', ')))))

# Closest coord count
c_c = {}


def get_closest_coord(x,y):
    dist = 1000
    c_res = [-1,-1]
    for c in s_c:
        d = abs(x-c[0]) + abs(y-c[1])
        if dist > d:
            dist = d
            c_res = c
        elif dist == d:
            c_res = [-1,-1]

    return tuple(c_res)

for x,y in product(range(1,max_size), range(1,max_size)):
    c = get_closest_coord(x,y)
    if c in c_c:
        c_c[c] += 1
    else:
        c_c[c] = 1


# Find infinites
x = 0
for y in range(0,max_size+1):
    c_c[get_closest_coord(x,y)] = 0

x = max_size+1
for y in range(0,max_size+1):
    c_c[get_closest_coord(x,y)] = 0

y = 0
for x in range(0,max_size+1):
    c_c[get_closest_coord(x,y)] = 0

y = max_size+1
for x in range(0,max_size+1):
    c_c[get_closest_coord(x,y)] = 0


print('Part 1: {0}'.format(max(list(c_c.values()))))


tot_max = 10000

def get_dist(xa,ya,xb,yb):
    return abs(xa-xb) + abs(ya-yb)

count = 0
for xa,ya in product(range(1,max_size), range(1,max_size)):
    dist_sum = 0
    for xb,yb in s_c:
        dist_sum += get_dist(xa,ya,xb,yb)
    if dist_sum < tot_max:
        count += 1

print('Part 2: {0}'.format(count))

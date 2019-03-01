import sys
import time

input = sys.stdin.read().rstrip()

rooms = {(0,0): set()}
opposite_room = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
move_x = {'N': 0, 'E': 1, 'S': 0, 'W': -1}
move_y = {'N': -1, 'E': 0, 'S': 1, 'W': 0}


start_time = time.time()

x = 0
y = 0
lvl = 0
lvls = {0: (0,0)}
for c in input[1:-1]:
    if c == '(':
        lvl += 1
        lvls[lvl] = (x,y)
    elif c == ')':
        x,y = lvls[lvl]
        del lvls[lvl]
        lvl -= 1
    elif c == '|':
        x,y = lvls[lvl]
    else:
        rooms[(x,y)].add(c)

        x += move_x[c]
        y += move_y[c]
        c = opposite_room[c]
        if (x,y) not in rooms:
            rooms[(x,y)] = {c}
        else:
            rooms[(x,y)].add(c)


dist = {(0,0): 0}
coord = {(0,0)}
d = 1
ans1 = 0
ans2 = 0
while coord:
    next_coord = set()
    for x,y in coord:
        for c in rooms[(x,y)]:
            xn = x + move_x[c]
            yn = y + move_y[c]
            if (xn,yn) not in dist:
                dist[(xn,yn)] = d
                next_coord.add((xn,yn))
                ans1 = d
                if d >= 1000:
                    ans2 += 1

    coord = next_coord
    d += 1


print('Part 1: {0}'.format(ans1))
print('Part 2: {0}'.format(ans2))
print('Time: {0}'.format(time.time() - start_time))


import time

start_time = time.time()

#depth: 5616
#target: 10,785

depth = 5616#510

xm = 0
ym = 0
mouth = (xm,ym)
xt = 10
yt = 785#10
target = (xt,yt)
cave = {mouth: 0, target: 0}
geo_idx = 0
erosion_lvl = 0

ans1 = 0
extx = 120
exty = 20
#100 50: [2000, 1062, 1063]
for x in range(xm,xt+extx):
    for y in range(ym,yt+exty):
        if (x,y) not in cave:
            if y == 0:
                geo_idx = 16807*x
            elif x == 0:
                geo_idx = 48271*y
            else:
                geo_idx = cave[(x-1,y)] * cave[(x,y-1)]
            erosion_lvl = (geo_idx + depth) % 20183
            cave[(x,y)] = erosion_lvl
            if x <= xt and y <= yt:
                ans1 += erosion_lvl % 3

gear = {0: {1,2}, 1: {0,2}, 2: {0,1}}
r = {}
for x in range(xm,xt+extx):
    for y in range(ym,yt+exty):
        cave[(x,y)] = cave[(x,y)] % 3        
        r[(x,y)] = {}
        for g in gear[cave[(x,y)]]:
            r[(x,y)][g] = 2000


def calc(t1, t2, g):
    if g not in gear[t2]:
        return -1,-1
    if t1 == 0 and t2 == 1 or t1 == 1 and t2 == 0:
        if g == 2:
            return g,1
        else:
            return 2,8
    elif t1 == 0 and t2 == 2 or t1 == 2 and t2 == 0:
        if g == 1:
            return g,1
        else:
            return g,8
    elif t1 == 1 and t2 == 2 or t1 == 2 and t2 == 1:
        if g == 0:
            return g,1
        else:
            return g,8
    else:
        return g,1


def update(x,y):
    global r

    u = set()

    for xn,yn in [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]:
        if (xn >= 0 and yn >= 0 and
            xn < xt+extx and yn < yt+exty):
            tl = [2000,2000,2000]
            gn = set()
            for gs in r[(x,y)]['g']:
                g,t = calc(cave[(x,y)],cave[(xn,yn)],gs)
                if g != -1 and t != -1:
                    t += r[(x,y)]['t'][gs]
                    tl[g] = min(tl[g],t)
                    gn.add(g)

            c = cave[(xn,yn)]
            if c == 0:
                tl[1] = min(tl[1],tl[2]+7)
                tl[2] = min(tl[1]+7,tl[2])
            elif c == 1:
                tl[0] = min(tl[0],tl[2]+7)
                tl[2] = min(tl[0]+7,tl[2])
            else:
                tl[0] = min(tl[0],tl[1]+7)
                tl[1] = min(tl[0]+7,tl[1])

            if (xn,yn) not in r:
                r[(xn,yn)] = {'g': gear[cave[(xn,yn)]], 't': tl}
                u.add((xn,yn))
            else:
                for i in range(3):
                    if tl[i] < r[(xn,yn)]['t'][i]:
                        if tl[i] < min(r[target]['t'])+7:
                            r[(xn,yn)]['g'].add(i)
                            r[(xn,yn)]['t'][i] = tl[i]
                            u.add((xn,yn))

    return u

r = {mouth: {'t': [2000,0,7], 'g': {1,2}}, target: {'t': [2000,2000,2000], 'g': {1,2}}}
u = {mouth}
def solve(u):
    while u:
        u2 = set()
        for c in u:
            x,y = c
            u2 = u2 | update(x,y)
        u = u2
        print(len(u))

x_min = 2000
y_min = 2000
for y in range(yt+exty):
    if min(r[(xt+extx-1,y)]['t']) < x_min:
        x_min = min(r[(xt+extx-1,y)]['t']) + abs(yt - y) + extx
for x in range(xt+extx):
    if min(r[(x,yt+exty-1)]['t']) < y_min:
        y_min = min(r[(x,yt+exty-1)]['t']) + abs(xt - x) + exty
print('{}, {}'.format(x_min,y_min))

ans2 = r[target]['t']
print('Part 1: {}'.format(ans1))
print('Part 2: {}'.format(ans2))
print('Time: {}'.format(time.time() - start_time))

import sys
import re


input = sys.stdin.read().rstrip().split('\n')

xs = len(input[0])
ys = len(input)

# 1 is wall, 0 is empty
m = [[0 for i in range(ys)] for j in range(xs)]

# key is position, ap is attack power, hp is hit points
e = {}
g = {}


for y,line in enumerate(input):
    for x,c in enumerate(line):
        if c == 'G':
            g[(x,y)] = {'ap': 3, 'hp': 200}
        elif c == 'E':
            e[(x,y)] = {'ap': 40, 'hp': 200}
        elif c == '#':
            m[x][y] = 1


# return set of all reachable coordinates for x, y
# sq at start should be an empty set
def reachable(x, y, sq):
    for xt,yt in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
        if ((xt,yt) not in sq and
            m[xt][yt] == 0 and
            (xt,yt) not in e and
            (xt,yt) not in g):
            sq.add((xt,yt))
            sq = reachable(xt, yt, sq)

    return sq


# return a 'map' where the value in each square is the distance to x, y
# occupied squares are set to -1
# mp[x][y] at start should be 0
def distance(x, y, mp):
    for xt,yt in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
        if (mp[xt][yt] > mp[x][y]+1 and
            m[xt][yt] == 0 and
            (xt,yt) not in e and
            (xt,yt) not in g):
            mp[xt][yt] = mp[x][y]+1
            mp = distance(xt, yt, mp)

    return mp


def move(soldier_x, soldier_y, allies, enemies):
    #print('{0} tries to move'.format((soldier_x,soldier_y)))
    # get all reachable squares
    sq = set()
    sq = reachable(soldier_x, soldier_y, sq)


    # remove squares that are not adjacent to an enemy
    for y in range(ys):
        for x in range(xs):
            adjacent_enemy = False
            for xt,yt in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
                if (xt,yt) in enemies:
                    adjacent_enemy = True
                    break

            if not adjacent_enemy and (x,y) in sq:
                sq.remove((x,y))

    # find closest enemy
    mp = [[100 for i in range(ys)] for j in range(xs)]
    mp[soldier_x][soldier_y] = 0
    mp = distance(soldier_x, soldier_y, mp)
    sq2 = set()
    dist = 100
    for s in sq:
        (x,y) = s
        if mp[x][y] < dist:
            sq2 = set()
            sq2.add((x,y))
            dist = mp[x][y]
        elif mp[x][y] == dist:
            sq2.add((x,y))

    closest_enemy = (0,0)
    for y in range(ys):
        for x in range(xs):
            if (x,y) in sq2:
                if closest_enemy == (0,0):
                    closest_enemy = (x,y)

    # find path to closest enemy
    closest = [100]*4
    (x,y) = closest_enemy
    mp = [[100 for i in range(ys)] for j in range(xs)]
    mp[x][y] = 0
    mp = distance(x, y, mp)
    #print('{0}'.format(mp))
    closest[0] = min(closest[0],mp[soldier_x][soldier_y-1])
    closest[1] = min(closest[1],mp[soldier_x-1][soldier_y])
    closest[2] = min(closest[2],mp[soldier_x+1][soldier_y])
    closest[3] = min(closest[3],mp[soldier_x][soldier_y+1])


    # move soldier
    if sq2:
        idx = closest.index(min(closest))
        new_coord = (0,0)
        if idx == 0:
            new_coord = (soldier_x, soldier_y-1)
        elif idx == 1:
            new_coord = (soldier_x-1, soldier_y)
        elif idx == 2:
            new_coord = (soldier_x+1, soldier_y)
        else:
            new_coord = (soldier_x, soldier_y+1)

        allies[new_coord] = allies[(soldier_x, soldier_y)].copy()
        del allies[(soldier_x, soldier_y)]
        #print('{0} -> {1}'.format((soldier_x,soldier_y),new_coord))
        return new_coord
    else:
        return (soldier_x, soldier_y)


# returns true if soldier performed an attack
def attack(soldier_x, soldier_y, allies, enemies):
    #print('{0} tries to attack'.format((soldier_x,soldier_y)))
    hp = [201]*4
    i = 0
    for xt,yt in [(soldier_x, soldier_y-1), (soldier_x-1, soldier_y), (soldier_x+1, soldier_y), (soldier_x, soldier_y+1)]:
        if (xt,yt) in enemies:
            hp[i] = enemies[(xt,yt)]['hp']
        i += 1

    if min(hp) < 201:
        i = hp.index(min(hp))
        coord = (0,0)
        if i == 0:
            coord = (soldier_x, soldier_y-1)
        elif i == 1:
            coord = (soldier_x-1, soldier_y)
        elif i == 2:
            coord = (soldier_x+1, soldier_y)
        else:
            coord = (soldier_x, soldier_y+1)

        if enemies[(coord)]['hp'] <= allies[(soldier_x, soldier_y)]['ap']:
            del enemies[(coord)]
            print('round {0}: {1} elves vs {2} goblins'.format(round, len(e),len(g)))
        else:
            enemies[(coord)]['hp'] -= allies[(soldier_x, soldier_y)]['ap']

        print('{0} attacked {1}'.format((soldier_x,soldier_y),coord))
        return True
    else:
        return False
        

def update(soldier_x, soldier_y, allies, enemies):
    if attack(soldier_x, soldier_y, allies, enemies):
        (x,y) = (soldier_x, soldier_y)
    else:
        (x,y) = move(soldier_x, soldier_y, allies, enemies)
        attack(x, y, allies, enemies)
    return (x,y)

print('{0} elves vs {1} goblins'.format(len(e),len(g)))
round = 1
corr = 0
while e and g:
    updated = set()
    for y in range(ys):
        for x in range(xs):
            if (x,y) in e and (x,y) not in updated:
                if not g:
                    corr = -1
                updated.add(update(x, y, e, g))
            elif (x,y) in g and (x,y) not in updated:
                if not e:
                    corr = -1
                updated.add(update(x, y, g, e))

    round += 1

print()
round = round+corr-1
print('round: {0}'.format(round))
print('elves: {0}'.format(len(e)))
print('goblins: {0}'.format(len(g)))
hp_sum = 0
for elf in e:
    hp_sum += e[elf]['hp']
for goblin in g:
    hp_sum += g[goblin]['hp']
print('hp_sum: {0}'.format(hp_sum))
print('outcome: {0}'.format(round*hp_sum))

for y in range(ys):
    s = ''
    hp = ''
    for x in range(xs):
        if (x,y) in g:
            s += 'G'
            hp += ' G('
            hp += str(g[(x,y)]['hp'])
            hp += ')'
        elif (x,y) in e:
            s += 'E'
            hp += ' E('
            hp += str(e[(x,y)]['hp'])
            hp += ')'
        elif m[x][y] == 1:
            s += '#'
        else:
            s += '.'
    print(s+hp)




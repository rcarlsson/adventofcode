import sys

# open ground: .
# tree: |
# lumberyard: #
input = sys.stdin.read().rstrip().split('\n')

xs = len(input[0])
ys = len(input)


l1 = [['' for y in range(ys)] for x in range(xs)]
l2 = [['' for y in range(ys)] for x in range(xs)]

for y,line in enumerate(input):
    for x,c in enumerate(line):
        l1[x][y] = c
        l2[x][y] = c

def get_adjacent(x,y,l):
    og = 0
    tr = 0
    ly = 0

    for xt,yt in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
        if xt >= 0 and xt < xs and yt >= 0 and yt < ys:
            if l[xt][yt] == '.':
                og += 1
            elif l[xt][yt] == '|':
                tr += 1
            elif l[xt][yt] == '#':
                ly += 1

    return og,tr,ly


cycle_length = 28 # calculated manually, after ~1000 iterations
tot_time = 1000000000
init_iter = 600
extra_iter = (tot_time - init_iter) % 28
count = []

i = 0
while i < (init_iter + extra_iter):
    if i % 2 == 0:
        l_old = l1
        l_new = l2
    else:
        l_old = l2
        l_new = l1

    for x in range(xs):
        for y in range(ys):
            og,tr,ly = get_adjacent(x,y,l_old)
            if l_old[x][y] == '.' and tr >= 3:
                l_new[x][y] = '|'
            elif l_old[x][y] == '|' and ly >= 3:
                l_new[x][y] = '#'
            elif l_old[x][y] == '#' and not (tr > 0 and ly > 0):
                l_new[x][y] = '.'

    for x in range(xs):
        for y in range(ys):
            l_old[x][y] = l_new[x][y]

    i += 1

    if i == 10:
        tr_tot = sum(x.count('|') for x in l1)
        ly_tot = sum(x.count('#') for x in l1)
        print('Part 1: {0}'.format(tr_tot*ly_tot))

    count.append(sum(x.count('|') for x in l1)*sum(x.count('#') for x in l1))

tr_tot = sum(x.count('|') for x in l1)
ly_tot = sum(x.count('#') for x in l1)
print('Part 2: {0}'.format(tr_tot*ly_tot))

for n,c in enumerate(count):
    print('{0}: {1}'.format(n,c))


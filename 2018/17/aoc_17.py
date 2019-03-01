import sys
import re

input = sys.stdin.read().rstrip().split('\n')

# 0 is empty, 1 is clay, 2 is running water, 3 is stable water
l = [[0 for i in range(2000)] for j in range(600)]
x_min = 1000
x_max = 0
y_min = 1000
y_max = 0

for line in input:
    a,b,c = list(map(int, re.findall(r'\d+', line)))
    if line[0] == 'x':
        for y in range(b,c+1):
            l[a][y] = 1
            x_min = min(a, x_min)
            x_max = max(a, x_max)
            y_min = min(b, y_min)
            y_max = max(c, y_max)
    elif line[0] == 'y':
        for x in range(b,c+1):
            l[x][a] = 1
            x_min = min(b, x_min)
            x_max = max(c, x_max)
            y_min = min(a, y_min)
            y_max = max(a, y_max)

def spread(x,y,l):
    l[x][y] = 2
    while (y < y_max and l[x][y+1] in [0,2]):
        l[x][y+1] = 2
        y += 1

    fillin = 3

    while fillin == 3 and y >= 0:
        xmin = x
        while (l[xmin-1][y] in [0,2] and l[xmin-1][y+1] in [1,3]):
            xmin -= 1

        xmax = x
        while (l[xmax+1][y] in [0,2] and l[xmax+1][y+1] in [1,3]):
            xmax += 1

        if (l[xmin-1][y] in [0,2] or
            l[xmin][y+1] in [0,2] or
            l[xmax+1][y] in [0,2] or
            l[xmax][y+1] in [0,2]):
            fillin = 2

        for xt in range(xmin,xmax+1):
            l[xt][y] = fillin

        y -= 1

    y += 1

    if y < y_max:
        if l[xmin-1][y] == 0:
            spread(xmin-1,y,l)
        if l[xmax+1][y] == 0:
            spread(xmax+1,y,l)

spread(500,1,l)

#for y in range(y_min,y_max+1):
#    s = ''
#    for x in range(x_min, x_max+1):
#        if l[x][y] == 1:
#            s += '#'
#        elif l[x][y] == 2:
#            s += '|'
#        elif l[x][y] == 3:
#            s += '~'
#        else:
#            s += '.'
#    print(s)

running = sum(x[y_min:y_max+1].count(2) for x in l)
stable = sum(x[y_min:y_max+1].count(3) for x in l)

print('Part 1: {0}'.format(running+stable))
print('Part 2: {0}'.format(stable))


import sys
import re

input = sys.stdin.read().rstrip().split('\n')

points = []
speed = []
letter_height = 10

for line in input:
    x,y,xv,yv = map(int, re.findall(r'[-+]?\d+', line))
    points.append([x,y])
    speed.append([xv,yv])

def find_x(y):
    xl = []
    for p in points:
        if p[1] is y:
            xl.append(p[0])
    return xl      

def print_points():
    xmax,xmin,ymax,ymin = get_corners()
    for y in range(ymin,ymax+1):
        xl = find_x(y)
        line = ''
        for x in range(xmin,xmax+1):
            if x in xl:
                line += '#'
            else:
                line += '.'
        print('{0}'.format(line))

def move_points():
    global points
    global speed
    for i,p in enumerate(points):
        p[0] += speed[i][0]
        p[1] += speed[i][1]

def get_corners():
    ymax = -100000
    ymin = 100000
    xmax = -100000
    xmin = 100000
    for x,y in points:
        ymax = max(ymax,y)
        ymin = min(ymin,y)
        xmax = max(xmax,x)
        xmin = min(xmin,x)
    return [xmax,xmin,ymax,ymin]

for s in range(100000):
    xmax,xmin,ymax,ymin = get_corners()
    if ymax-ymin <= letter_height:
        print('Part 1:')
        print_points()
        print('Part 2: {0}\n'.format(s))
    move_points()




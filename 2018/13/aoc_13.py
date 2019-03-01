import sys
import re
import time
start = time.time()

input = sys.stdin.read().rstrip().split('\n')
#right is 0
def_cart = {'dir': 0, 'turns': 0}
rails = {}
carts = {}
def_rail = {'type': ''}
x_size = len(input[0])
y_size = len(input)

for y,line in enumerate(input):
    for x,c in enumerate(line):
        cart = None
        part = ''
        if c is '<':
            cart = {'dir': 2, 'turns': 0}
            if y < y_size-1 and input[y+1][x] in 'v^|/\\' and \
                y > 0 and input[y-1][x] in 'v^|/\\':
                part = '+'
            elif y < y_size-1 and input[y+1][x] in 'v^|/\\':
                part = '\\'
            elif y > 0 and input[y-1][x] in 'v^|/\\':
                part = '/'
            else:
                part = '-'

        elif c is '>':
            cart = {'dir': 0, 'turns': 0}
            if y < y_size-1 and input[y+1][x] in 'v^|/\\' and \
                y > 0 and input[y-1][x] in 'v^|/\\':
                part = '+'
            elif y < y_size-1 and input[y+1][x] in 'v^|/\\':
                part = '/'
            elif y > 0 and input[y-1][x] in 'v^|/\\':
                part = '\\'
            else:
                part = '-'
        elif c is 'v':
            cart = {'dir': 1, 'turns': 0}
            if x < x_size-1 and line[x+1] in '<>-/\\' and \
                x > 0 and line[x-1] in '<>-/\\':
                part = '+'
            elif x < x_size-1 and line[x+1] in '<>-/\\':
                part = '/'
            elif x > 0 and line[x-1] in '<>-/\\':
                part = '\\'
            else:
                part = '|'
        elif c is '^':
            cart = {'dir': 3, 'turns': 0}
            if x < x_size-1 and line[x+1] in '<>-/\\' and \
                x > 0 and line[x-1] in '<>-/\\':
                part = '+'
            elif x < x_size-1 and line[x+1] in '<>-/\\':
                part = '\\'
            elif x > 0 and line[x-1] in '<>-/\\':
                part = '/'
            else:
                part = '|'
        elif c is ' ':
            part = None;
        else:
            part = c

        if part:
            rails[(x,y)] = part
        if cart:
            carts[(x,y)] = cart

def rotate_cart(coord):
    global carts
    cart = carts[coord]
    if rails[coord] is '/':
        if cart['dir'] is 0:
            carts[coord]['dir'] = 3
        elif cart['dir'] is 1:
            carts[coord]['dir'] = 2
        elif cart['dir'] is 2:
            carts[coord]['dir'] = 1
        elif cart['dir'] is 3:
            carts[coord]['dir'] = 0
    elif rails[coord] is '\\':
        if cart['dir'] is 0:
            carts[coord]['dir'] = 1
        elif cart['dir'] is 1:
            carts[coord]['dir'] = 0
        elif cart['dir'] is 2:
            carts[coord]['dir'] = 3
        elif cart['dir'] is 3:
            carts[coord]['dir'] = 2
    elif rails[coord] is '+':
        if cart['turns'] is 0:
            carts[coord]['dir'] = (cart['dir']-1)%4
        elif cart['turns'] is 2:
            carts[coord]['dir'] = (cart['dir']+1)%4
        carts[coord]['turns'] = (cart['turns']+1)%3

def move_cart(x,y):
    global carts
    cart = carts[(x,y)]
    if cart['dir'] is 0:
        new_coord = (x+1,y)
    elif cart['dir'] is 1:
        new_coord = (x,y+1)
    elif cart['dir'] is 2:
        new_coord = (x-1,y)
    elif cart['dir'] is 3:
        new_coord = (x,y-1)
    
    if new_coord in carts:
        print('Time {0}: Collision at {1}'.format(t, new_coord))
        del carts[(x,y)]
        del carts[new_coord]
    else:
        carts[new_coord] = {'dir': cart['dir'], 'turns': cart['turns']}
        del carts[(x,y)]
        rotate_cart(new_coord)
    return new_coord

print('{0} carts at start'.format(len(carts)))
t = 0
while len(carts) > 1:
    moved = set()
    for x in range(x_size):
        for y in range(y_size):
            if (x,y) in carts and (x,y) not in moved:
                moved.add(move_cart(x,y))
    t += 1

for key in carts:
    print('Last remaining cart: {0}'.format(key))

end = time.time()
print(end - start)


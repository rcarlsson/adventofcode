import sys

input = sys.stdin.read().rstrip().split('\n')

_,_,initial_state = input[0].split()

rules = {}

for rule in input[2:]:
    key,_,value = rule.split()
    r = 0
    for i,c in enumerate(key):
        if c is '#':
            r += 1 << (4-i)
    if value is '#':
        rules[r] = 1
    else:
        rules[r] = 0

def_pot = {'v': 0, 'prev': None, 'next': None}
pots = {}
start = 0
end = len(initial_state)-1

for i,c in enumerate(initial_state):
    pot = def_pot.copy()
    if i > 0:
        pot['prev'] = pots[i-1]
    
    if c is '#':
        pot['v'] = 1

    pots[i] = pot.copy()
    if i > 0:        
        pots[i-1]['next'] = pots[i]

def extend_pots(beginning):
    global start
    global end
    global pots

    if beginning:
        for i in range(5):
            pots[start-1] = {'v': 0, 'prev': None, 'next': pots[start]}
            pots[start]['prev'] = pots[start-1]
            start -= 1
    else:
        for i in range(5):
            pots[end+1] = {'v': 0, 'prev': pots[end], 'next': None}
            pots[end]['next'] = pots[end+1]
            end += 1

extend_pots(True)
extend_pots(False)

sums = set()

def calc_sum():
    tmp = 0
    for i in range(start,end+1):
        if pots[i]['v'] is 1:
           tmp += i
    return tmp 

for t in range(1000):
    update = set()
    prev_sum = calc_sum()

    mask = (pots[start]['v'] << 3) + (pots[start+1]['v'] << 2) + (pots[start+2]['v'] << 1) + pots[start+3]['v']
    for i in range(start+2,end-1):
        mask = ((mask << 1) & 0x1F) + pots[i+2]['v']
        if mask in rules:
            if (rules[mask] is not pots[i]['v']):
                update.add(i)
        elif (0 is not pots[i]['v']):
            update.add(i)


    for i in update:
        pots[i]['v'] = (pots[i]['v'] + 1) % 2

    if pots[start]['v']+pots[start+1]['v']+pots[start+2]['v']+pots[start+3]['v']+pots[start+4]['v'] > 0:
        extend_pots(True)

    if pots[end]['v']+pots[end-1]['v']+pots[end-2]['v']+pots[end-3]['v']+pots[end-4]['v'] > 0:
        extend_pots(False)

    s = ''
    for i in range(start,end+1):
        if pots[i]['v'] is 1:
            s += '#'
        else:
            s += '.'

    new_sum = calc_sum()
    print('{0}: {1} ({2})'.format(t+1, new_sum, new_sum-prev_sum))
    if new_sum in sums:
        print('{0}'.format(t+1))
        #break
    sums.add(new_sum)

print('{0}'.format(60598+59*(50000000000-1000)))


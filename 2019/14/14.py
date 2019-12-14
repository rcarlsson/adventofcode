import sys
import os
import copy

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

lines = [line.rstrip('\n') for line in open(file_name)]

reactions = {}
for line in lines:
    l = line.replace(',','').split(' ')
    i = {}
    for idx in range(0,len(l)-3,2):
        i[l[idx+1]] = int(l[idx])
    reactions[l[-1]] = {'o': int(l[-2]), 'i': i}

def calc_ore(fuel=1):
    inp = {k: reactions['FUEL']['i'][k] * fuel for k in reactions['FUEL']['i']}
    stash = {}

    while len(inp) > 1:
        newinp = {}
        newinp['ORE'] = inp.get('ORE',0)
        for k in inp:
            if k == 'ORE':
                continue
            n = inp[k] # needed

            # if possible, take all chemicals from stash
            if stash.get(k,0) >= n:
                stash[k] -= n
                continue

            n -= stash.get(k,0) # take available chemicals from stash
            p = reactions[k]['o'] # produced per reaction
            c = (n-1)//p + 1 # how many reactions are needed
            stash[k] =  p*c-n # add leftover to stash

            # replace needed chemical with its reaction input
            for ki in reactions[k]['i']:
                newinp[ki] = newinp.get(ki,0) + c * reactions[k]['i'][ki]

        inp = newinp.copy()
    return inp['ORE']

print("Part 1: {}".format(calc_ore()))

(fmin,fmax) = (1,sys.maxsize)
while fmin != fmax:
    fuel = (fmax-fmin-1)/2 + fmin
    (fmin,fmax) = (fuel+1,fmax) if calc_ore(fuel) <= 1000000000000 else (fmin,fuel)
print("Part 2: {}".format(fuel))
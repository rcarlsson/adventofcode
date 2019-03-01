import sys
from itertools import product
import string

s = sys.stdin.read().rstrip().split('\n')
r1 = {}
r2 = {}
for r in s:
    if r[5] not in r1:
        r1[r[5]] = []
        r2[r[5]] = []
    if r[36] not in r1:
        r1[r[36]] = [r[5]]
        r2[r[36]] = [r[5]]
    else:
        r1[r[36]].append(r[5])
        r2[r[36]].append(r[5])

order = ""

while bool(r1):

    for c in sorted(r1):
        if not r1[c]:
            order += c
            r1.pop(c)
            for c_rm in r1:
                if c in r1[c_rm]:
                    r1[c_rm].remove(c)
            break


print('Part 1: {0}'.format(order))

n_workers = 5
available = [0]*n_workers
ongoing = ['-']*n_workers
step_time = 60
time = 0
tick = True

while bool(r2):
    tick = True

    for w_idx,c_done in enumerate(ongoing):
        if c_done is not '-' and available[w_idx] <= time:
            r2.pop(c_done)
            for c_rm in r2:
                if c_done in r2[c_rm]:
                    r2[c_rm].remove(c_done)
            ongoing[w_idx] = '-'
            tick = False

    if time >= min(available):
        w_idx = available.index(min(available))

        for c_new in sorted(r2):
            if not r2[c_new] and c_new not in ongoing:
                ongoing[w_idx] = c_new
                available[w_idx] = time + step_time + ord(c_new)-ord('A')+1
                tick = False
                break

    if tick:
        time+=1


print('Part 2: {0}'.format(max(available)))

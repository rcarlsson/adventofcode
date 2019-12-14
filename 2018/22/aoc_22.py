import sys

depth = 5616
target = 10 + 785j

er = {}
for x in range(0,int(target.real)+1):
    er[x] = (x*16807 + depth) % 20183

for y in range(0,int(target.imag)+1):
    er[y*1j] = (y*48271 + depth) % 20183

er[0] = 0
er[target] = (0 + depth) % 20183

for x in range(1,int(target.real)+1):
    for y in range(1,int(target.imag)+1):
        c = x + 1j*y
        if c not in er:
            er[c] = (er[c-1]*er[c-1j] + depth) % 20183

print(sum([er[c]%3 for c in er]))

# 0 = nothing, 1 = torch, 2 = climbing gear
# rocky -> cl.gr/torch
# wet -> cl.gr/neither
# narrow -> torch/neither

# move -> 1 minute
# switch gear -> 7 minutes
# switch to torch at target

allowed_tools = {0: [1,2], 1: [2,0], 2: [1,0]}

def extend_er(p):
    global er
    x = int(p.real)
    y = int(p.imag)
    if p-1 in er:
        er[x] = (x*16807 + depth) % 20183
        p = x + 1j
        while p-1 in er:
            er[p] = (er[p-1]*er[p-1j] + depth) % 20183
            p += 1j
    else:
        er[y*1j] = (y*48271 + depth) % 20183
        p = 1 + y*1j
        while p-1j in er:
            er[p] = (er[p-1]*er[p-1j] + depth) % 20183
            p += 1


d = {}
d[(0,1)] = 0
def update_adj(pos, tool):
    global d
    adj_pos = [pos-1, pos-1j, pos+1, pos+1j]
    updated = set()
    for p in adj_pos:
        if p.real < 0 or p.imag < 0:
            continue
        if p not in er:
            extend_er(p)
        if tool not in allowed_tools[er[p]%3]:
            continue
        if (p,tool) not in d or d[(pos,tool)]+1 < d[(p,tool)]:
            d[(p,tool)] = d[(pos,tool)]+1
            updated.add((p,tool))

    for t in allowed_tools[er[pos]%3]:
        if t == tool:
            continue
        if (pos,t) not in d or d[(pos,tool)]+7 < d[(pos,t)]:
            d[(pos,t)] = d[(pos,tool)]+7
            updated.add((pos,t))

    if (target,1) in updated:
        print(d[(target,1)])
    return updated

d = {}
d[(0,1)] = 0
d[(target,1)] = sys.maxsize
x = set()
x.add((0,1))
while x:
    (pos,tool) = sorted(x, key=lambda i: d[i])[0]
    x.remove((pos,tool))
    diff = target-pos
    diff_manhattan = (int(abs(diff.real) + abs(diff.imag)))
    if d[(pos,tool)] + diff_manhattan < d[(target,1)]:
        x = x.union(update_adj(pos,tool))
        print(len(x))

print(d[target,1])
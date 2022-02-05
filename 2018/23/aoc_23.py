import sys
import re

def get_manhattan_distance(p, q):
    """ 
    Return the manhattan distance between points p and q
    assuming both to have the same number of dimensions
    """
    # sum of absolute difference between coordinates
    distance = 0
    for p_i,q_i in zip(p,q):
        distance += abs(p_i - q_i)
    
    return distance

file_name = sys.argv[1]

nanobots = {}
with open(file_name) as f:
    for line in f:
        line = line.replace("pos=<","")
        line = line.replace(">","")
        line = line.replace(" r=","")
        input = list(map(int, line.split(',')))
        nanobots[(input[0], input[1], input[2])] = input[3]

strongest = max(nanobots, key=nanobots.get)
radius = nanobots[strongest]

within_range = 0
mn = [999999999,999999999,999999999]
mx = [-999999999,-999999999,-999999999]
for nb in nanobots:
    if get_manhattan_distance(nb, strongest) <= radius:
        within_range += 1
    
    for i in range(3):
        mn[i] = min(mn[i], nb[i])
        mx[i] = max(mx[i], nb[i])

print("Part 1: {}".format(within_range))

def is_reachable(block, nanobot, reach):
    (bs, bx, by, bz) = block
    (nx, ny, nz) = nanobot

    if nx < bx + bs and nx >= bx and ny < by + bs and ny >= by and nz < bz + bs and nz >= bz:
        return True

    if nx < bx + bs and nx >= bx and ny < by + bs and ny >= by:
        if nz < bz:
            return get_manhattan_distance((nx, ny, bz), nanobot) <= reach
        else:
            return get_manhattan_distance((nx, ny, bz + bs - 1), nanobot) <= reach

    if nx < bx + bs and nx >= bx and nz < bz + bs and nz >= bz:
        if ny < by:
            return get_manhattan_distance((nx, by, nz), nanobot) <= reach
        else:
            return get_manhattan_distance((nx, by + bs - 1, nz), nanobot) <= reach

    if ny < by + bs and ny >= by and nz < bz + bs and nz >= bz:
        if nx < bx:
            return get_manhattan_distance((bx, ny, nz), nanobot) <= reach
        else:
            return get_manhattan_distance((bx + bs - 1, ny, nz), nanobot) <= reach
    
    if nx < bx + bs and nx >= bx:
        if ny < by and nz < bz:
            return get_manhattan_distance((nx, by, bz), nanobot) <= reach
        elif ny < by and nz >= bz + bs:
            return get_manhattan_distance((nx, by, bz + bs - 1), nanobot) <= reach
        elif nz < bz:
            return get_manhattan_distance((nx, by + bs - 1, bz), nanobot) <= reach
        else:
            return get_manhattan_distance((nx, by + bs - 1, bz + bs - 1), nanobot) <= reach

    if ny < by + bs and ny >= by:
        if nx < bx and nz < bz:
            return get_manhattan_distance((bx, ny, bz), nanobot) <= reach
        elif nx < bx and nz >= bz + bs:
            return get_manhattan_distance((bx, ny, bz + bs - 1), nanobot) <= reach
        elif nz < bz:
            return get_manhattan_distance((bx + bs - 1, ny, bz), nanobot) <= reach
        else:
            return get_manhattan_distance((bx + bs - 1, ny, bz + bs - 1), nanobot) <= reach

    if nz < bz + bs and nz >= bz:
        if nx < bx and ny < by:
            return get_manhattan_distance((bx, by, nz), nanobot) <= reach
        elif nx < bx and ny >= by + bs:
            return get_manhattan_distance((bx, by + bs - 1, nz), nanobot) <= reach
        elif ny < by:
            return get_manhattan_distance((bx + bs - 1, by, nz), nanobot) <= reach
        else:
            return get_manhattan_distance((bx + bs - 1, by + bs - 1, nz), nanobot) <= reach

    if nx < bx and ny < by and nz < bz:
        return get_manhattan_distance((bx, by, bz), nanobot) <= reach
    elif nx < bx and ny < by:
        return get_manhattan_distance((bx, by, bz + bs - 1), nanobot) <= reach
    elif nx < bx and nz < bz:
        return get_manhattan_distance((bx, by + bs - 1, bz), nanobot) <= reach
    elif ny < by and nz < bz:
        return get_manhattan_distance((bx + bs - 1, by, bz), nanobot) <= reach
    elif nx < bx:
        return get_manhattan_distance((bx, by + bs - 1, bz + bs - 1), nanobot) <= reach
    elif ny < by:
        return get_manhattan_distance((bx + bs - 1, by, bz + bs - 1), nanobot) <= reach
    elif nz < bz:
        return get_manhattan_distance((bx + bs - 1, by + bs - 1, bz), nanobot) <= reach
    else:
        return get_manhattan_distance((bx + bs - 1, by + bs - 1, bz + bs - 1), nanobot) <= reach

def get_reachable(block, nanobots):
    reachable = {}
    for nb in nanobots:
        if is_reachable(block, nb, nanobots[nb]):
            reachable[nb] = nanobots[nb]

    return reachable

xd = mx[0] - mn[0]
yd = mx[1] - mn[1]
zd = mx[2] - mn[2]

blocks = {}
blocks[(max(max(xd, yd), zd)+1, mn[0], mn[1], mn[2])] = nanobots
blk = (max(max(xd, yd), zd)+1, mn[0], mn[1], mn[2])
best_point = (0, 0, 0)
reach_count = 0

next_blk = None
while True:
    blk = None
    if next_blk is not None:
        blk = next_blk
    else:
        remove = set()
        for b in blocks:
            if len(blocks[b]) >= reach_count:
                blk = b
                break
            else:
                remove.add(b)
        for r in remove:
            blocks.pop(r)
    
    if blk is None:
        print("Part 2:", get_manhattan_distance((0, 0, 0), best_point))
        exit(0)
    
    (s, x, y, z) = blk

    # Break it down to 8 smaller blocks
    s = (s+1)//2

    new_blks = [
        (s, x, y, z),
        (s, x+s, y, z),
        (s, x, y+s, z),
        (s, x, y, z+s),
        (s, x+s, y+s, z),
        (s, x+s, y, z+s),
        (s, x, y+s, z+s),
        (s, x+s, y+s, z+s),
    ]

    next_blk = None
    length = 0
    for new_blk in new_blks:
        res = get_reachable(new_blk, blocks[blk])

        if len(res) < reach_count:
            continue

        if s == 1:
            if len(res) > reach_count or len(res) == reach_count and get_manhattan_distance((0, 0, 0), (new_blk[0], new_blk[1], new_blk[2])) < get_manhattan_distance((0, 0, 0), best_point):
                best_point = (new_blk[1], new_blk[2], new_blk[3])
                reach_count = len(res)
        else:
            if len(res) > length:
                length = len(res)
                next_blk = new_blk

            blocks[new_blk] = res

    # Remove old block
    blocks.pop(blk)

import sys


d = sys.stdin.read().rstrip().split()
d = list(map(int, d))


children = {}
data = {}
nodesum = 0

def get_node(idx):
    global children
    global data
    n_children = d[idx]
    n_data = d[idx+1]

    next_idx = idx+2
    for n in range(n_children):
        if idx in children:
            children[idx].append(next_idx)
        else:
            children[idx] = [next_idx]
        next_idx = get_node(next_idx)

    data[idx] = d[next_idx:next_idx+n_data]
    return next_idx+n_data

get_node(0)

print('Part 1: {0}'.format(sum(sum(l) for l in data.values())))

def node_sum(idx):
    result = 0

    if idx not in children:
        return sum(data[idx])

    for i in data[idx]:
        if i <= len(children[idx]):
            result += node_sum(children[idx][i-1])

    return result    


print('Part 2: {0}'.format(node_sum(0)))



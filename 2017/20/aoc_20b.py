import sys
from functools import reduce
from operator import itemgetter


def update_dot(pos, vel, acc):
    for idx in range(len(pos)):
        vel[idx] += acc[idx]
        pos[idx] += vel[idx]


def get_closest_dot(positions):
    distance = 1000000000000
    result = 0

    for idx in range(len(positions)):
        tmp_dist = reduce((lambda x, y: abs(x) + abs(y)), positions[idx])
        if tmp_dist < distance:
            distance = tmp_dist
            result = idx

    return result


def check_collisions(idx, positions):
    collisions = set()
    for idx2 in range(idx+1, len(positions)):
        if positions[idx] == positions[idx2]:
            collisions.add(idx)
            collisions.add(idx2)

    return collisions


def solve(file_name):
    positions = []
    velocities = []
    accelerations = []
    max_time = 1000
    ticks = 0

    with open(file_name) as f:
        for line in f:
            line = line.replace('p=<', '')
            line = line.replace('>, v=<', ' ')
            line = line.replace('>, a=<', ' ')
            line = line.replace('>', '')
            pos, vel, acc = line.split()
            positions.append(list(map(int, pos.split(','))))
            velocities.append(list(map(int, vel.split(','))))
            accelerations.append(list(map(int, acc.split(','))))

    while ticks < max_time:
        collisions = set()
        for idx in range(len(positions)):
            collisions = collisions.union(check_collisions(idx, positions))

        collisions = sorted(collisions)
        collisions.reverse()
        for idx in collisions:
            positions.pop(idx)
            velocities.pop(idx)
            accelerations.pop(idx)

        for idx in range(len(positions)):
            update_dot(positions[idx], velocities[idx], accelerations[idx])

        if ticks % (max_time/100) == 0:
            print('{0}% done, count={1}'.format(int(ticks*100/max_time), len(positions)))

        ticks += 1

    return len(positions)


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

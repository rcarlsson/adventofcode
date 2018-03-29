import sys
from functools import reduce


def update_dot(pos, vel, acc):
    for idx in range(len(pos)):
        pos[idx] += vel[idx]
        vel[idx] += acc[idx]


def get_closest_dot(positions):
    distance = 1000000000000
    result = 0

    for idx in range(len(positions)):
        tmp_dist = reduce((lambda x, y: abs(x) + abs(y)), positions[idx])
        if tmp_dist < distance:
            distance = tmp_dist
            result = idx

    return result


def solve(file_name):
    positions = []
    velocities = []
    accelerations = []
    ticks = 1000

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

    while ticks:
        for idx in range(len(positions)):
            update_dot(positions[idx], velocities[idx], accelerations[idx])


        ticks -= 1

    return get_closest_dot(positions)


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()

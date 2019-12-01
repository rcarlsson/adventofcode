import sys
import math

file_name = sys.argv[1]

masses = [int(line.rstrip('\n')) for line in open(file_name)]
res1 = 0
res2 = 0

for m in masses:
    res1 += int((math.floor(m / 3)) - 2)

print("Part 1: {}".format(res1))

for m in masses:
    while True:
        m = int((math.floor(m / 3)) - 2)
        if m > 0:
            res2 += m
        else:
            break

print("Part 2: {}".format(res2))
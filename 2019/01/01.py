import sys
import os
import math

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

masses = [int(line.rstrip('\n')) for line in open(file_name)]

fuel1 = [m//3 - 2 for m in masses]
print("Part 1: {}".format(sum(fuel1)))

fuel2 = 0
for f in fuel1:
    while f > 0:
        fuel2 += f
        f = f//3 - 2
print("Part 2: {}".format(fuel2))
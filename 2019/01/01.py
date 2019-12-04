import sys
import os
import math

file_name = ''

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    # If no file provided, try to find 'input' in script folder
    path = os.path.realpath(__file__).rsplit('/',1)[0]
    file_name = path+'/input'

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
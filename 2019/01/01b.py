import sys
import math

file_name = sys.argv[1]

lines = [line.rstrip('\n') for line in open(file_name)]
res = 0

for line in lines:
    x = int(line)
    while True:
        x = int((math.floor(x / 3)) - 2)
        if x > 0:
            res += x
        else:
            break

print(res)
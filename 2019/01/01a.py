import sys
import math

file_name = sys.argv[1]

lines = [line.rstrip('\n') for line in open(file_name)]
res = 0

for line in lines:
    res += int((math.floor(int(line) / 3)) - 2)

print(res)
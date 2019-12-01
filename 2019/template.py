import sys

file_name = sys.argv[1]

lines = [line.rstrip('\n') for line in open(file_name)]
res1 = 0
res2 = 0

for line in lines:
    print(line)

print("Part 1: {}".format(res1))
print("Part 2: {}".format(res2))
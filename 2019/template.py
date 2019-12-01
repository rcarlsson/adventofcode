import sys

file_name = sys.argv[1]

lines = [line.rstrip('\n') for line in open(file_name)]
res = 0

for line in lines:
    print(line)

print(res)
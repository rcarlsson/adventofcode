import sys
import os

file_name = ''

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    # If no file provided, try to find 'input' in script folder
    path = os.path.realpath(__file__).rsplit('/',1)[0]
    file_name = path+'/input'

lines = [line.rstrip('\n') for line in open(file_name)]
res1 = 0
res2 = 0

for line in lines:
    print(line)

print("Part 1: {}".format(res1))
print("Part 2: {}".format(res2))
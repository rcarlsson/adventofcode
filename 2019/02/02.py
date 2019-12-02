import sys

file_name = sys.argv[1]

lines = [line.rstrip('\n') for line in open(file_name)]

data = [int(x) for x in lines[0].split(',')]

data[1] = 12
data[2] = 2

for x in range(0, len(data), 4):
    op = data[x]
    if op == 99:
        break

    addr1 = data[x+1]
    addr2 = data[x+2]
    res_addr = data[x+3]

    if op == 1:
        data[res_addr] = data[addr1] + data[addr2]
    elif op == 2:
        data[res_addr] = data[addr1] * data[addr2]

print("Part 1: {}".format(data[0]))

#  0, 0 -> 29848
# +1, 0 -> +307200
#  0,+1 -> +1
# wanted result = 19690720
x = 19690720 - 29848
verb = x % 307200
noun = (x-verb) / 307200
print("Part 2: {}".format(100*noun + verb))
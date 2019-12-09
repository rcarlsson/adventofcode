import sys
import os

sys.path.append('../')
import intcode

file_name = ''

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    # If no file provided, try to find 'input' in script folder
    path = os.path.realpath(__file__).rsplit('/',1)[0]
    file_name = path+'/input'

init_prog = [int(x) for x in open(file_name).read().split(',')]

program = init_prog[:]
ip = 0
res1 = 0
while True:
    (tmp_res, ip, _) = intcode.run(program, [1], ip)
    if tmp_res is None:
        break
    else:
        res1 = tmp_res
print("Part 1: {}".format(res1))

program = init_prog[:]
ip = 0
res2 = 0
while True:
    (tmp_res, ip, _) = intcode.run(program, [5], ip)
    if tmp_res is None:
        break
    else:
        res2 = tmp_res
print("Part 2: {}".format(res2))

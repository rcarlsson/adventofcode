import sys
import os

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

(l, u) = map(int, open(file_name).read().split('-'))

pwds1 = set()
for x in range(l,u+1):
    pwd = str(x)
    if pwd[0] <= pwd[1] <= pwd[2] <= pwd[3] <= pwd[4] <= pwd[5] and \
        max([pwd[i] == pwd[i+1] for i in range(5)]):
            pwds1.add(pwd)

print("Part 1: {}".format(len(pwds1)))

pwds2 = set()
for pwd in pwds1:
    x = ' ' + pwd + ' '
    if max([x[i] == x[i+1] and x[i] != x[i-1] and x[i+1] != x[i+2] for i in range(1, len(x)-1)]):
        pwds2.add(pwd)

print("Part 2: {}".format(len(pwds2)))
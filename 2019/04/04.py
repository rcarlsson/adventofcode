import sys

# Limits given by problem
l = 147981
u = 691423

# Store all passwords that are:
# - within the limits
# - increasing
# - have at least two adjacent equal numbers
pwds1 = set()
for x in range(l,u+1):
    x_str = str(x)

    if x_str[0] <= x_str[1] and x_str[1] <= x_str[2] and x_str[2] <= x_str[3] and x_str[3] <= x_str[4] and x_str[4] <= x_str[5]:
        if x_str[0] == x_str[1] or x_str[1] == x_str[2] or x_str[2] == x_str[3] or x_str[3] == x_str[4] or x_str[4] == x_str[5]:
            pwds1.add(x_str)

print("Part 1: {}".format(len(pwds1)))

# Find all stored passwords that do not have exactly two adjacent equal numbers
pwds2 = set()
for pwd in pwds1:
    x = ' ' + pwd + ' '
    for i in range(1, len(x)-1):
        if x[i] == x[i+1] and x[i] != x[i-1] and x[i+1] != x[i+2]:
            pwds2.add(pwd)
            break

print("Part 2: {}".format(len(pwds2)))
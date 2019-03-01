import sys
import re
import itertools
import math

n = 300
m = 300
sqr_val = [0] * n
sqr_agr_val = [0] * n
for i in range(n):
    sqr_val[i] = [0] * m
    sqr_agr_val[i] = [0] * m

serial_nr = 1309

def power_level(x,y):
    pwr = ((x+10)*y+serial_nr)*(x+10)
    pwr = pwr % 1000
    pwr = math.floor(pwr / 100)
    pwr = pwr - 5
    return pwr

for x in range(300):
    for y in range(300):
        sqr_val[x][y] = power_level(x,y)

max_val = -10000
x_ans = 0
y_ans = 0
s_ans = 0

sqr_agr_val[299][299] = sqr_val[299][299]

for x in range(299,-1,-1):
    for y in range(299,-1,-1):
        if x < 299 and y < 299:
            sqr_agr_val[x][y] = sqr_agr_val[x+1][y] + sqr_agr_val[x][y+1] - sqr_agr_val[x+1][y+1] + sqr_val[x][y]
        elif x < 299:
            sqr_agr_val[x][y] = sqr_agr_val[x+1][y] + sqr_val[x][y]
        elif y < 299:
            sqr_agr_val[x][y] = sqr_agr_val[x][y+1] + sqr_val[x][y]


#print('sqr_agr_val: {0}'.format(sqr_agr_val))
for s in range(300):
    print('2: s: {0}'.format(s))
    for x in range(300-s):
        for y in range(300-s):
            #print('{0} - {1} - {2} + {3}'.format(sqr_agr_val[x][y],sqr_agr_val[x+s][y],sqr_agr_val[x][y+s],sqr_agr_val[x+s][y+s]))
            val = sqr_agr_val[x][y]-sqr_agr_val[x+s][y]-sqr_agr_val[x][y+s]+sqr_agr_val[x+s][y+s]

            #print('val: {0}'.format(val))
            if max_val < val:
                max_val = val
                x_ans = x
                y_ans = y
                s_ans = s

print('Part 2: {0},{1},{2}\n'.format(x_ans,y_ans,s_ans))




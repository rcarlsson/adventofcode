import sys
import os

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

image = [line.rstrip('\n') for line in open(file_name)][0]

width = 25
height = 6
l_size = width*height

z_count = [l.count('0') for l in [image[i:i+l_size] for i in range(0,len(image),l_size)]]
li = z_count.index(min(z_count))*l_size
print("Part 1: {}".format(image[li:li+l_size].count('1')*image[li:li+l_size].count('2')))

res_layer = ['2' for _ in range(l_size)]
for li in range(0,len(image),l_size):
    res_layer = [image[li+i] if p == '2' else p for i,p in enumerate(res_layer)]

print("Part 2:")
for r in range(0,l_size,width):
    print(''.join(res_layer[r:r+width]).replace('1','#').replace('0',' '))
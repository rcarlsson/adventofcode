import sys
import os

file_name = ''

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    # If no file provided, try to find 'input' in script folder
    path = os.path.realpath(__file__).rsplit('/',1)[0]
    file_name = path+'/input'

image = [line.rstrip('\n') for line in open(file_name)][0]

width = 25
height = 6
l_size = width*height
l_min = {'idx': 0, 'z_count': sys.maxsize}
res_layer = ['2' for _ in range(l_size)]

for l_start in range(0, len(image), l_size):
    layer = image[l_start:l_start+l_size]

    zero_count = layer.count('0')
    if zero_count < l_min['z_count']:
        l_min['idx'] = l_start
        l_min['z_count'] = zero_count

    for idx in range(l_size):
        if res_layer[idx] == '2':
            res_layer[idx] = layer[idx]

min_layer = image[l_min['idx']:l_min['idx']+l_size]
print("Part 1: {}".format(min_layer.count('1')*min_layer.count('2')))

# 0 = black
# 1 = white
# 2 = transparent
print_l = ''.join(res_layer)
print_l = print_l.replace('2', ' ')
print_l = print_l.replace('1', '#')
print_l = print_l.replace('0', '.')
print("Part 2:")
for row_idx in range(0, len(print_l), width):
    print(print_l[row_idx:row_idx+width])

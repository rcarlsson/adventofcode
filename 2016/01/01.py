import sys

x = 0
y = 0
# 0=north, 1=east ...
facing_direction = 0
file_name = sys.argv[1]
path = [[0,0]] 

def walk(distance):
	global x
	global y
	
	# print('walking {0} blocks (dir={1})'.format(distance, facing_direction))

	for i in range(0,distance):
		if facing_direction is 0:
			y += 1
		elif facing_direction is 1:
			x += 1
		elif facing_direction is 2:
			y -= 1
		elif facing_direction is 3:
			x -= 1
		
		# if [x,y] in path:
			# print('paths crossed at [{0},{1}]'.format(x,y))

		path.append([x,y])

def rotate(direction):
	global facing_direction

	if direction is 'L':
		# print('rotating left')
		facing_direction-=1
	elif direction is 'R':
		# print('rotating right')
		facing_direction+=1
	
	facing_direction = facing_direction%4

with open(file_name) as f:
    for line in f:
    	line = line.replace(" ", "").rstrip()
        data_array = line.split(",")
        for data in data_array:
        	# print('instruction: {0}'.format(data))
        	rotate(data[0])
        	walk(int(data[1:]))
        	
    print('result: x={0}, y={1}, sum={2}'.format(x,y,abs(x)+abs(y)))


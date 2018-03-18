import sys

x = 1
y = 3
valid_positions = [[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,2,3,4,0,0],[0,5,6,7,8,9,0],[0,0,'A','B','C',0,0],[0,0,0,'D',0,0,0],[0,0,0,0,0,0,0]]
file_name = sys.argv[1]

def print_value(row,col):
	print valid_positions[row][col]

def valid(row,col):
	return valid_positions[row][col] != 0

def move(direction):
	global x
	global y

	if direction is 'U' and valid(y-1,x):
		y -= 1
	elif direction is 'D' and valid(y+1,x):
		y += 1
	elif direction is 'L' and valid(y,x-1):
		x -= 1
	elif direction is 'R' and valid(y,x+1):
		x += 1

with open(file_name) as f:
    for line in f:
    	line = line.replace(" ", "").rstrip()
        for c in line:
        	move(c)
        
        print_value(y,x)

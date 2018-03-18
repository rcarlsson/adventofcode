import sys

file_name = sys.argv[1]

count = 0

def valid_triangle(a,b,c):

	if a+b > c and a+c > b and b+c > a:
		return True
	else:
		return False


with open(file_name) as f:
	row = 0
	data_array = [0,0,0]
	for line in f:
		row += 1
		line = " ".join(line.split())
		data_array[row%3] = line.split(" ")

		if row%3 is 0:
			for col in range(3):
				if valid_triangle(int(data_array[0][col]), int(data_array[1][col]), int(data_array[2][col])):
					count += 1 	
    
	print('found {0} valid triangles'.format(count))


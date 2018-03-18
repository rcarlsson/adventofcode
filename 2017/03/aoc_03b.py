import sys

def accumulate(matrix, x, y):
	sum = matrix[x-1][y-1] + matrix[x][y-1] + matrix[x+1][y-1] + matrix[x-1][y] + matrix[x+1][y] + matrix[x-1][y+1] + matrix[x][y+1] + matrix[x+1][y+1]
	matrix[x][y] = sum
	return sum

def solve(value):
	max_size = 10
	sqr_size = 1
	Matrix = [[0 for x in range(max_size)] for y in range(max_size)]
	Matrix[2][2] = 1

	x_s = 2
	y_s = 2
	sqr_size += 2
	x_cur = 2
	y_cur = 2
	while sqr_size<=max_size:
		y_cur+=1

		for x in range(x_cur,x_cur+(sqr_size-1)):
			rv = accumulate(Matrix, x, y_cur)
			if rv > value:
				return rv

		x_cur += sqr_size-2
		y_cur -= 1

		for y in range(y_cur,y_cur-(sqr_size-1),-1):
			rv = accumulate(Matrix, x_cur, y)
			if rv > value:
				return rv

		y_cur -= sqr_size-2
		x_cur -= 1
	
		for x in range(x_cur,x_cur-(sqr_size-1),-1):
			rv = accumulate(Matrix, x, y_cur)
			if rv > value:
				return rv

		x_cur -= sqr_size-2
		y_cur +=1

		for y in range(y_cur,y_cur+(sqr_size-1)):
			rv = accumulate(Matrix, x_cur, y)
			if rv > value:
				return rv

		y_cur += sqr_size-2

		sqr_size += 2
		

	return value

def main():
	input = int(sys.argv[1])
	output = solve(input)
	print('{0}'.format(output))

if __name__ == "__main__":
    main()
import sys

sum = 0
file_name = sys.argv[1]

with open(file_name) as f:
	for line in f:
		c_prev = -1
		for c in line:
			if c is c_prev:
				sum += int(c)
			c_prev = c

		if line[0] is line[-2]:
			sum += int(line[0])

		print('sum={0}'.format(sum))

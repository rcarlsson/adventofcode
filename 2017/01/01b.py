import sys

sum = 0
file_name = sys.argv[1]

with open(file_name) as f:
	for line in f:
		size = len(line)-1
		for idx in range(0,size):
			if line[idx] is line[(idx+size/2)%size]:
				sum += int(line[idx])

		print('sum={0}'.format(sum))

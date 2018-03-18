import sys

sum = 0
file_name = sys.argv[1]

with open(file_name) as f:
	for line in f:

		line = line.rstrip()
		data_array = sorted(map(int,line.split("\t")))
		size = len(data_array)

		for idx1 in range(0,size):
			for idx2 in range(idx1+1,size):
				if data_array[idx2]%data_array[idx1] is 0:
					sum += data_array[idx2]/data_array[idx1]
					break

	print('sum={0}'.format(sum))

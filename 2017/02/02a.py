import sys

sum = 0
file_name = sys.argv[1]

with open(file_name) as f:
	for line in f:
		max = 0
		min = 10000

		line = line.rstrip()
		data_array = line.split("\t")

		for data in data_array:
			data_int = int(data)
			if data_int > max:
				max = data_int
			if data_int < min:
				min = data_int

		sum += max - min

	print('sum={0}'.format(sum))

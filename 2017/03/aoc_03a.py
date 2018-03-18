import sys

def calcPathLength(value):

	if value == 1:
		return 0

	sqr_size = 3

	while sqr_size**2 < value:
		sqr_size+=2


	tmp_val = value - (sqr_size-2)**2

	tmp_val = abs(tmp_val - sqr_size//2)

	tmp_val = tmp_val%(sqr_size-1)

	if tmp_val > sqr_size//2:
		tmp_val = sqr_size-1 - tmp_val

	while tmp_val > sqr_size//2:
		tmp_val -= sqr_size//2

	result = sqr_size//2 + tmp_val

	return result

def main():
	input = int(sys.argv[1])
	output = calcPathLength(input)
	print('{0}'.format(output))

if __name__ == "__main__":
    main()

import sys

def solve(jumps):
	count = 0
	idx = 0
	while True:
		jumps[idx] += 1
		idx += jumps[idx] - 1
		count += 1		
		if idx < 0 or idx >= len(jumps):
			return count

def main():
	file_name = sys.argv[1]
	jumps = []
	with open(file_name) as f:
		for line in f:
			jumps.append(int(line))
	output = solve(jumps)
	print('{0}'.format(output))

if __name__ == "__main__":
    main()

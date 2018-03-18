import sys

def solve(file_name):
	count = 0
	line_count = 0
	with open(file_name) as f:
		for line in f:
			line_count += 1
			words = line.split()
			for idx in range(len(words)):
				words[idx] = sorted(words[idx])
			for word in words:
				if words.count(word) > 1:
					count += 1
					break
	return line_count - count

def main():
	file_name = sys.argv[1]
	output = solve(file_name)
	print('{0}'.format(output))

if __name__ == "__main__":
    main()

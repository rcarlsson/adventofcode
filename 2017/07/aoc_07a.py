import sys
import re

def solve(f):
	programs = []
	for line in f:
		line = re.sub("\(.*?\)", "", line)
		line = re.sub("->", "", line)
		line = re.sub(",", "", line)
		programs += line.split()

	for program in programs:
		if programs.count(program) == 1:
			return program

def main():
	file_name = sys.argv[1]
	with open(file_name) as f:
		output = solve(f)
	print('{0}'.format(output))

if __name__ == "__main__":
    main()
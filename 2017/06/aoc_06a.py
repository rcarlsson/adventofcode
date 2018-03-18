import sys

def solve(mem_list):
	seen_before = []
	length = len(mem_list)

	while mem_list not in seen_before:
		seen_before.append(list(mem_list))
		idx = mem_list.index(max(mem_list))
		value = mem_list[idx]
		mem_list[idx] = 0
		for x in range(value):
			mem_list[(idx+x+1)%length] += 1

	return len(seen_before)
	
def main():
	file_name = sys.argv[1]
	with open(file_name) as f:
		for line in f:
			input = list(map(int, line.split()))
			output = solve(input)
			print('{0}'.format(output))

if __name__ == "__main__":
    main()
import sys


file_name = sys.argv[1]
line_length = 8
count = [[0 for x in range(26)] for y in range(line_length)]
message = ""

with open(file_name) as f:
    for line in f:
    	line = line.replace(" ", "").rstrip()
        for idx in range(line_length):
			char = line[idx]
			char_idx = ord(char) - ord('a')
			count[idx][char_idx] += 1

for x in range(line_length):
	for y in range(26):
		if count[x][y] == 0:
			count[x][y] = 99999

for idx in range(line_length):
	message += chr(count[idx].index(min(count[idx]))+ord('a'))

print message

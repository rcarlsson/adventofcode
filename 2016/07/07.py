import sys

file_name = sys.argv[1]
count = 0

def containsABBA(text):
	print text
	for idx in range(len(text)-3):
		if text[idx] != text[idx+1]:
			if text[idx] == text[idx+3]:
				if text[idx+1] == text[idx+2]:
					return True
	return False


with open(file_name) as f:
    for line in f:
		line = line.replace(" ", "").rstrip()
		abba = False
		print line
		while True:
			if line.find('[') == -1:
				abba |= containsABBA(line)
				break

			idx = line.index('[')
			abba |= containsABBA(line[:idx])
			line = line[idx+1:]

			idx = line.index(']')
			if containsABBA(line[:idx]):
				abba = False
				break
			else:
				line = line[idx+1:]

		print abba
		print "------------------"
		if abba:
			count += 1
			
print count

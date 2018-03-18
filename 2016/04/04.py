import sys

file_name = sys.argv[1]
nr_of_letters = ord('z')-ord('a')+1
letter_count = [0] * nr_of_letters

def calculate_checksum():
	global letter_count
	correct_checksum = ""
	for i in range(5):
		idx = letter_count.index(max(letter_count))
		correct_checksum += chr(idx+ord('a'))
		letter_count[idx] = 0
	return correct_checksum

with open(file_name) as f:
    for line in f:
		line = line.replace(" ", "").rstrip()
		checksum = line[-6:-1]
		sector_id = int(line[-10:-7])
		room_name = line[:-11].replace("-"," ")

		for char in range(ord('a'),ord('z')):
			letter_count[char-ord('a')] = room_name.count(chr(char))

		if checksum == calculate_checksum():
			correct_name = ""
			for char in room_name:
				if char != ' ':
					char_int = ord(char)
					char_int += sector_id%nr_of_letters
					if char_int > ord('z'):
						char_int -= nr_of_letters
					char = chr(char_int)
				correct_name += char

			if "object" in correct_name:
				print('{0} {1}'.format(correct_name, str(sector_id)))

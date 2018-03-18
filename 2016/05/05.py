import md5
import sys

door_name = sys.argv[1]
idx = 0
password = ['-'] * 8

def done():
	rv = True
	for i in password:
		if i == '-':
			rv = False

	return rv

while not(done()):
	m = md5.new()
	m.update(door_name + str(idx))
	if m.hexdigest()[:5] == "00000" and m.hexdigest()[5] < '8':
		if password[int(m.hexdigest()[5])] == '-':
			password[int(m.hexdigest()[5])] = m.hexdigest()[6]
			print('idx: {0} md5: {1}'.format(idx, m.hexdigest()))

	idx += 1

print password

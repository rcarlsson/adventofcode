import sys
import re

def calc_weight(program, weights, tower):
	weight = weights[program]
	for sub_tower in tower:
		if sub_tower[0] == program:
			if len(sub_tower) > 1:
				for sub_program in sub_tower[1:]:
					weight += calc_weight(sub_program, weights, tower)
			break

	return weight

def check_balance(program, weights, tower):
	balance_ok = True
	weight = weights[program]
	tower_weights = []

	for sub_tower in tower:
		if sub_tower[0] == program:
			if len(sub_tower) > 1:
				for sub_program in sub_tower[1:]:
					check_balance(sub_program, weights, tower)
					tower_weights.append(calc_weight(sub_program, weights, tower))
				
				if sum(tower_weights) != tower_weights[0]*len(tower_weights):
					balance_ok = False
					print('{0}:'.format(program))
					for idx in range(len(tower_weights)):
						print('{0}: {1}'.format(sub_tower[idx+1], tower_weights[idx]))
					print('---------------')
			break

			
	return balance_ok


def solve(f):
	weights = []
	programs = []

	for line in f:
		line = re.sub("->", "", line)
		line = re.sub(",", "", line)
		tuple = line.split()[0], int(line.replace('(','').replace(')','').split()[1])
		weights.append(tuple)

		line = re.sub("\(.*?\)", "", line)
		programs.append(line.split())

	weights = dict(weights)

	for program in programs:
		if programs.count(program) == 1:
			check_balance(program[0], weights, programs)

def main():
	file_name = sys.argv[1]
	with open(file_name) as f:
		solve(f)

if __name__ == "__main__":
    main()
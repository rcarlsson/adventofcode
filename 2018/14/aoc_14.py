import sys
import re

#input = sys.stdin.read().rstrip().split('\n')

recipes = [3,7]
recipe_length = 2
elf1 = 0
elf2 = 1

def add_recipes():
    global recipe_length
    global elf1
    global elf2

    new_recipe = recipes[elf1] + recipes[elf2]
    if new_recipe > 9:
        recipes.append(1)
        recipe_length += 1
    recipes.append(new_recipe % 10)
    recipe_length += 1
    elf1 = (elf1 + 1 + recipes[elf1]) % recipe_length
    elf2 = (elf2 + 1 + recipes[elf2]) % recipe_length

    if elf2 is elf1:
        elf2 += 1

ans = 0

def check_sequence():
    global ans
    if recipes[-6:] is [8,8,0,7,5,1] or \
        recipes[-7:-1] is [8,8,0,7,5,1]:
        #why does this not work...
        return True
    if recipes[recipe_length-1] is 1 and \
        recipes[recipe_length-2] is 5 and \
        recipes[recipe_length-3] is 7 and \
        recipes[recipe_length-4] is 0 and \
        recipes[recipe_length-5] is 8 and \
        recipes[recipe_length-6] is 8:
        ans = recipe_length-6
        return True
    elif recipes[recipe_length-2] is 1 and \
        recipes[recipe_length-3] is 5 and \
        recipes[recipe_length-4] is 7 and \
        recipes[recipe_length-5] is 0 and \
        recipes[recipe_length-6] is 8 and \
        recipes[recipe_length-7] is 8:
        ans = recipe_length-7
        return True
    else:
        return False

while not check_sequence():
    add_recipes()
    #print('{0}, {1}'.format(recipes, recipe_length))

#s = ''
#for i in range(10):
#    s += str(recipes[recipe_length-10+i])
#for i in range(recipe_length):
#    s += str(recipes[i])
print('Part 2: {0}'.format(ans))


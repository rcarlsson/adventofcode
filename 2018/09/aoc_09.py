import sys
import re

num_of_players,last_marble = map(int, re.findall(r'\d+', sys.stdin.read()))

players = [0]*num_of_players
marbles = {0: [0, 0]}
current = 0

def move(curr, clockwise, steps):
    for _ in range(steps):
        if clockwise:
            curr = marbles[curr][0]
        else:
            curr = marbles[curr][1]
    return curr

for marble in range(1,last_marble+1):
    if marble % 23 is 0:
        player = marble%len(players)
        current = move(current, False, 7)
        players[player] += marble
        players[player] += current

        prev = marbles[current][1]
        next = marbles[current][0]
        marbles[prev][0] = next
        marbles[next][1] = prev
        current = next
    else:
        current = move(current, True, 1)
        marbles[marble] = [marbles[current][0], current]
        marbles[marbles[current][0]][1] = marble
        marbles[current][0] = marble
        current = marble

print('Part 1: {0}'.format(max(players)))


players = [0]*num_of_players
marbles = {0: [0, 0]}
current = 0

for marble in range(1,last_marble*100+1):
    if marble % 23 is 0:
        player = marble%len(players)
        current = move(current, False, 7)
        players[player] += marble
        players[player] += current

        prev = marbles[current][1]
        next = marbles[current][0]
        marbles[prev][0] = next
        marbles[next][1] = prev
        current = next
    else:
        current = move(current, True, 1)
        marbles[marble] = [marbles[current][0], current]
        marbles[marbles[current][0]][1] = marble
        marbles[current][0] = marble
        current = marble

print('Part 2: {0}'.format(max(players)))



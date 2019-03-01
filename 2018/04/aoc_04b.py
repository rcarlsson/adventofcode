import sys
import re


input = sys.stdin.read()
input = input.strip().split('\n')
input.sort()


guards = []
start = 0
stop = 0

for idx, item in enumerate(input):

    if "Guard" in input[idx]:
        yr,mo,dy,h,m,id = [int(n) for n in re.findall('\d+',input[idx])]
        if id not in guards:
            guards.append(id)


start = 0
stop = 0
g = 0
m = 0
c = 0

for guard in guards:
    sleeping = {}
    correct_guard = False

    for idx, item in enumerate(input):
        if "Guard" in input[idx]:
            yr,mo,dy,h,min,id = [int(n) for n in re.findall('\d+',input[idx])]
            correct_guard = (id == guard)

        if correct_guard and "asleep" in input[idx]:
            yr,mo,dy,h,start = [int(n) for n in re.findall('\d+',input[idx])]

        elif correct_guard and "wakes up" in input[idx]:
            yr,mo,dy,h,stop = [int(n) for n in re.findall('\d+',input[idx])]
            for minute in range(start,stop):
                if minute not in sleeping:
                    sleeping[minute] = 1
                else:
                    sleeping[minute] += 1

    print('{0}'.format(guard))
    print('{0}'.format(sleeping))
    v=list(sleeping.values())
    k=list(sleeping.keys())
    if v and k:
        minute = k[v.index(max(v))]
        print('{0}'.format(minute))
        print('{0}'.format(sleeping[minute]))
        print('{0}\n'.format(m))
        if sleeping[minute] > c:
            g = guard
            m = minute
            c = sleeping[minute]

print('{0}'.format(g))
print('{0}'.format(m))
print('{0}'.format(c))
print('{0}'.format(g*m))

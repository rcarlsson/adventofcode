import sys
import re


input = sys.stdin.read()
input = input.strip().split('\n')
input.sort()


guards = {}
sleeping = {}
start = 0
stop = 0

for idx, item in enumerate(input):

    if "Guard" in input[idx]:
        yr,mo,dy,h,m,id = [int(n) for n in re.findall('\d+',input[idx])]
        if id not in guards:
            guards[id] = 0

    elif "asleep" in input[idx]:
        yr,mo,dy,h,start = [int(n) for n in re.findall('\d+',input[idx])]

    elif "wakes up" in input[idx]:
        yr,mo,dy,h,stop = [int(n) for n in re.findall('\d+',input[idx])]
        guards[id] += stop-start

v=list(guards.values())
k=list(guards.keys())
guard = k[v.index(max(v))]
index = 0

start = 0
stop = 0
for idx, item in enumerate(input):

    if "Guard" in input[idx]:
        yr,mo,dy,h,m,id = [int(n) for n in re.findall('\d+',input[idx])]
        if id == guard:
            index = idx+1
            break

correct_guard = False
for idx, item in enumerate(input):
    if "Guard" in input[idx]:
        yr,mo,dy,h,m,id = [int(n) for n in re.findall('\d+',input[idx])]
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

    index += 1

v=list(sleeping.values())
k=list(sleeping.keys())
minute = k[v.index(max(v))]
print('{0}'.format(guards))
print('{0}'.format(sleeping))
print('{0}'.format(guard))
print('{0}'.format(minute))
print('{0}'.format(guard*minute))

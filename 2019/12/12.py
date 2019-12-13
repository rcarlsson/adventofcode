import sys
import os
from itertools import combinations
from operator import add,sub
from numpy import lcm
from functools import reduce

file_name = os.path.realpath(__file__).rsplit('/',1)[0]+'/input'

if len(sys.argv) > 1:
    file_name = sys.argv[1]

lines = [line.rstrip('\n') for line in open(file_name)]

class Moon:
    def __init__(self, pos):
        self.p = pos
        self.v = [0 for _ in range(len(pos))]

    def move(self):
        self.p = map(add,self.p,self.v)
    
    def copy(self):
        m = Moon(self.p[:])
        m.v = self.v[:]
        return m

class SolarSystem:
    def __init__(self):
        self.moons = []
        self.start = []
        self.time = 0

    def add_moon(self,moon):
        self.moons.append(moon)
        self.start.append(moon.copy())

    def apply_gravity(self):
        sign = lambda a: 0 if a == 0 else a/abs(a)
        for (m1,m2) in combinations(self.moons,2):
            diff = map(sign,map(sub,m1.p,m2.p))
            m1.v = map(sub,m1.v,diff)
            m2.v = map(add,m2.v,diff)

    def apply_velocity(self):
        for m in self.moons:
            m.move()

    def tick(self, n=1):
        for _ in range(n):
            self.apply_gravity()
            self.apply_velocity()
        self.time += n
        return self

    def get_total_energy(self):
        return sum([sum(map(abs,m.p))*sum(map(abs,m.v)) for m in self.moons])

    def check_state(self):
        res = [True for _ in range(len(self.moons[0].p))]
        for j in range(len(res)):
            for i in range(len(self.moons)):
                m = self.moons[i]
                c = self.start[i]
                if m.p[j] != c.p[j] or m.v[j] != c.v[j]:
                    res[j] = False
                    break
        return res

s = SolarSystem()
for line in lines:
    s.add_moon(Moon([int(l.strip(' <>xyz=')) for l in line.split(',')]))

print("Part 1: {}".format(s.tick(1000).get_total_energy()))

periods = [sys.maxsize for _ in range(len(s.moons[0].p))]
while max(periods) == sys.maxsize:
    periods = [periods[i] if not st else min(periods[i],s.time) for i,st in enumerate(s.tick().check_state())]

print("Part 2: {}".format(reduce(lcm,periods)))
from enum import Enum

class Result(Enum):
    HALT = 99
    INPUT = 3
    OUTPUT = 4

class IntCode:
    def __init__(self, program, inp=None):
        self.program = program[:]
        self.ip = 0
        self.rel_ptr = 0
        self.inp = inp[:] if inp else []
        self.out = []

    def get_out(self):
        return self.out[:]

    def give_inp(self, inp):
        self.inp.append(inp)

    def get_reg(self, idx):
        return self.program[idx]

    def run(self):
        while True:

            if self.ip >= len(self.program)-3:
                self.program += [0 for _ in range(self.ip-len(self.program)+4)]

            op = self.program[self.ip] % 100
            m1 = (self.program[self.ip] // 100) % 10
            m2 = (self.program[self.ip] // 1000) % 10
            m3 = (self.program[self.ip] // 10000) % 10

            if m1 == 0:
                p1 = self.program[self.ip+1]
            elif m1 == 1:
                p1 = self.ip+1
            elif m1 == 2:
                p1 = self.program[self.ip+1]+self.rel_ptr

            if m2 == 0:
                p2 = self.program[self.ip+2]
            elif m2 == 1:
                p2 = self.ip+2
            elif m2 == 2:
                p2 = self.program[self.ip+2]+self.rel_ptr

            if m3 == 0:
                p3 = self.program[self.ip+3]
            elif m3 == 1:
                p3 = self.ip+3
            elif m3 == 2:
                p3 = self.program[self.ip+3]+self.rel_ptr

            if op in [1,2,3,4,5,6,7,8,9] and p1 >= len(self.program):
                self.program += [0 for _ in range(p1-len(self.program)+1)]
            if op in [1,2,5,6,7,8] and p2 >= len(self.program):
                self.program += [0 for _ in range(p2-len(self.program)+1)]
            if op in [1,2,7,8] and p3 >= len(self.program):
                self.program += [0 for _ in range(p3-len(self.program)+1)]

            if op == 99:
                return Result.HALT
            if op == 1:
                self.program[p3] = self.program[p1] + self.program[p2]
                self.ip += 4
            elif op == 2:
                self.program[p3] = self.program[p1] * self.program[p2]
                self.ip += 4
            elif op == 3:
                if self.inp:
                    self.program[p1] = self.inp.pop(0)
                    self.ip += 2
                else:
                    return Result.INPUT
            elif op == 4:
                self.ip += 2
                self.out.append(self.program[p1])
                return Result.OUTPUT
            elif op == 5:
                self.ip = self.program[p2] if self.program[p1] != 0 else self.ip+3
            elif op == 6:
                self.ip = self.program[p2] if self.program[p1] == 0 else self.ip+3
            elif op == 7:
                self.program[p3] = 1 if self.program[p1] < self.program[p2] else 0
                self.ip += 4
            elif op == 8:
                self.program[p3] = 1 if self.program[p1] == self.program[p2] else 0
                self.ip += 4
            elif op == 9:
                self.rel_ptr += self.program[p1]
                self.ip += 2
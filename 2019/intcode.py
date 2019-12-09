
# Runs until code 4 (output) or code 99 (halt).
# Returns output (or None if code 99), plus current ip and rel_ptr.
# Pads program with zeroes if ip gets too big.
# Crashes if input list is too short.
def run(program, inp=None, ip=0, rel_ptr=0):
    out = None
    while True:

        if ip >= len(program)-3:
            program += [0 for _ in range(ip-len(program)+4)]

        op = program[ip] % 100
        m1 = (program[ip] // 100) % 10
        m2 = (program[ip] // 1000) % 10
        m3 = (program[ip] // 10000) % 10

        if m1 == 0:
            p1 = program[ip+1]
        elif m1 == 1:
            p1 = ip+1
        elif m1 == 2:
            p1 = program[ip+1]+rel_ptr

        if m2 == 0:
            p2 = program[ip+2]
        elif m2 == 1:
            p2 = ip+2
        elif m2 == 2:
            p2 = program[ip+2]+rel_ptr

        if m3 == 0:
            p3 = program[ip+3]
        elif m3 == 1:
            p3 = ip+3
        elif m3 == 2:
            p3 = program[ip+3]+rel_ptr

        if op in [1,2,3,4,5,6,7,8,9] and p1 >= len(program):
            program += [0 for _ in range(p1-len(program)+1)]
        if op in [1,2,5,6,7,8] and p2 >= len(program):
            program += [0 for _ in range(p2-len(program)+1)]
        if op in [1,2,7,8] and p3 >= len(program):
            program += [0 for _ in range(p3-len(program)+1)]

        if op == 99:
            break
        if op == 1:
            program[p3] = program[p1] + program[p2]
            ip += 4
        elif op == 2:
            program[p3] = program[p1] * program[p2]
            ip += 4
        elif op == 3:
            program[p1] = inp.pop(0)
            ip += 2
        elif op == 4:
            ip += 2
            out = program[p1]
            break
        elif op == 5:
            ip = program[p2] if program[p1] != 0 else ip+3
        elif op == 6:
            ip = program[p2] if program[p1] == 0 else ip+3
        elif op == 7:
            program[p3] = 1 if program[p1] < program[p2] else 0
            ip += 4
        elif op == 8:
            program[p3] = 1 if program[p1] == program[p2] else 0
            ip += 4
        elif op == 9:
            rel_ptr += program[p1]
            ip += 2

    return (out, ip, rel_ptr)
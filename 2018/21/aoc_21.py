r3 = 0
r5 = 0
r3_hist = []
r5_updated = False
ans1 = 0
ans2 = 0

while True:
    if r5_updated:
        r5_updated = False
    else:
        r5 = r3 | 0x10000
        r3 = 5557974

    r3 = (((r3 + (r5 & 0xFF)) & 0xFFFFFF) * 65899) & 0xFFFFFF
    if r5 < 256:
        if r3 in r3_hist:
            break
        else:
            r3_hist.append(r3)
    else:
        r5 = (r5 >> 8)
        r5_updated = True

ans1 = r3_hist[0]
ans2 = r3_hist[-1]
print('Part 1: {}'.format(ans1))
print('Part 2: {}'.format(ans2))


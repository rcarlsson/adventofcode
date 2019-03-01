import sys


input = sys.stdin.read().strip()

def reduce_string(s):
    idx = 0
    while idx < len(s)-1:
        if abs(ord(s[idx]) - ord(s[idx+1])) == ord('a') - ord('A'):
            s = s[:idx] + s[(idx+2):]
            if idx > 0:
                idx -= 1
        else:
            idx += 1
    return s

a1 = len(reduce_string(input))
print('Part 1: {0}'.format(a1))


str_len = {}

for c in range(ord('A'),ord('Z')+1):
    s_tmp = input
    s_tmp = s_tmp.replace(chr(c),"")
    s_tmp = s_tmp.replace(chr(c-ord('A')+ord('a')),"")
    s_tmp = reduce_string(s_tmp)
    str_len[chr(c)] = len(s_tmp)

a2 = str_len[min(str_len, key = lambda x: str_len.get(x))]
print('Part 2: {0}'.format(a2))

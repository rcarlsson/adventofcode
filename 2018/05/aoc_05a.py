import sys


s = sys.stdin.read()

cont = True

while cont:
    cont = False    
    for idx, c in enumerate(s):
        if idx == len(s) - 1:
            break

        if abs(ord(s[idx]) - ord(s[idx+1])) == ord('a') - ord('A'):
            s = s[:idx] + s[(idx+2):]
            cont = True
            break

# -1 because newline at the end
print('{0}'.format(len(s)-1))

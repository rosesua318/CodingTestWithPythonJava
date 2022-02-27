import sys
str = sys.stdin.read()
ch = [0] * 26

for c in str :
    if c.islower() :
        ch[ord(c) - 97] += 1
for i in range(26) :
    if ch[i] == max(ch) :
        print(chr(i + 97), end='')

a, b, c = map(int, input().split())
n = 0
m = 0

if a % c :
    n = a // c + 1
else:
    n = a // c
if b % c:
    m = b // c + 1
else:
    m = b // c

print(n * m)

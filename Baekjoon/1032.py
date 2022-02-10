import sys

n = int(sys.stdin.readline())
a = list(sys.stdin.readline())

for _ in range(n-1):
    b = list(sys.stdin.readline())
    for i in range(len(a)):
        if a[i]!=b[i]:
            a[i] = "?"
            
print(''.join(a))

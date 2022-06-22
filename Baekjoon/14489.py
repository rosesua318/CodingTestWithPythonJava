a, b = map(int, input().split())
c = int(input())
n = 2 * c

if (a + b) >= n:
    print(a + b - n)
else:
    print(a + b)

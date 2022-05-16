import math

a, b, c = map(int, input().split())
s = (a + 1) * (b + 1) / (c + 1) - 1
print(math.floor(s))

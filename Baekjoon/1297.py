a, b, c = map(int, input().split())
d = a / ((b ** 2 + c ** 2) ** 0.5)
e = b * d
f = c * d
print(int(e), int(f))

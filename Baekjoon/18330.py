a = int(input())
b = int(input())

c = min(a, b + 60)
d = c * 1500 + (a - c) * 3000
print(d)

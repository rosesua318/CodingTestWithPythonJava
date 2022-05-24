import math

a = []
for i in range(5) :
    a.append(int(input()))
n = a[0] - max(math.ceil(a[1] / a[3]), math.ceil(a[2] / a[4]))

print(n)

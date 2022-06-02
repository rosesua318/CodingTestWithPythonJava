a = []
for i in range(5) :
    a.append(int(input()))

b = a[0] * a[4]
c = 0
if a[4] <= a[2]:
    c = a[1]
else:
    c = a[1] + (a[4] - a[2]) * a[3]
    
print(min(b, c))

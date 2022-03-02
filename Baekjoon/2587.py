n = []
for i in range(5) :
    n.append(int(input()))
print(sum(n) // 5)
n.sort()
print(n[2])

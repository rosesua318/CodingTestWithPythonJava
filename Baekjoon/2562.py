ns = []

for i in range(9) :
    n = int(input())
    ns.append(n)
    
maxN = max(ns)
index = ns.index(maxN) + 1

print(maxN)
print(index)

ns = []

for i in range(10) :
    ns.append(int(input()))

print(sum(ns) // 10)
print(max(ns, key = ns.count))

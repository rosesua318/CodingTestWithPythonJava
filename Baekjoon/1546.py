n = int(input())
sc = list(map(int, input().split()))

ms = max(sc)

final = []
for i in range(n) :
    final.append(sc[i] / ms*100)
avg = sum(final) / n
print("%.2f" % avg)

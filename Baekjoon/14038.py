li = []
for _ in range(6) :
    li.append(input())
n = li.count('W')
if n >= 5:
    print(1)
elif n >= 3:
    print(2)
elif n >= 1:
    print(3)
else:
    print(-1)

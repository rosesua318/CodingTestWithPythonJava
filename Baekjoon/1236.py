a, b = map(int, input().split())
array = []

for i in range(a) :
    array.append(input())

rc = 0
cc = 0

for i in range(a) :
    if 'X' not in array[i] :
        rc += 1

for j in range(b) :
    if 'X' not in [array[i][j] for i in range(a)] :
        cc += 1

print(max(rc, cc))

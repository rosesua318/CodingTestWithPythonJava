n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    even = []
    for j in a :
        if j % 2 == 0 :
            even.append(j)
    print(sum(even), min(even))

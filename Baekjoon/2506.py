n = int(input())
a = list(map(int, input().split()))
sum = 0
bonus = 0

for i in a :
    if i == 1 :
        sum += 1 + bonus
        bonus += 1
    else :
        bonus = 0

print(sum)

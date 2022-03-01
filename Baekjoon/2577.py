a = int(input())
b = int(input())
c = int(input())

mu = list(str(a * b * c))

nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for m in mu :
    nums[int(m)] += 1
for n in nums :
    print(n)

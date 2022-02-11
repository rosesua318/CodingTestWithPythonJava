a = list(map(int, input().split()))
b = min(a)

while True :
    count = 0
    for n in a :
        if b % n == 0 :
            count += 1
    if count >= 3 :
        print(b)
        break
    b += 1

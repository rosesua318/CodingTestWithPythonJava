n = int(input())
temp = n
count = 0

while True :
    a = temp // 10
    b = temp % 10
    sum = a + b
    
    temp = int(str(b) + str(sum % 10))
    count += 1
    
    if n == temp :
        break

print(count)

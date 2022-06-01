a = int(input())

if a % 10 != 0:
    print(-1)
else:
    print((a // 300), ((a % 300) // 60), ((a % 300 % 60) // 10), sep=' ')

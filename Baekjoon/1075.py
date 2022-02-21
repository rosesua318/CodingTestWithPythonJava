a = list(input())
b = int(input())

a[-2:] = ['0'] * 2
a = int(''.join(a))

while a % b != 0 :
    a += 1

print(str(a)[-2:])

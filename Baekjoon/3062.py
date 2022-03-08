n = int(input())

for _ in range(n) :
    s = input()
    a = str(int(s) + int(s[::-1]))
    if a == a[::-1] :
        print("YES")
    else :
        print("NO")

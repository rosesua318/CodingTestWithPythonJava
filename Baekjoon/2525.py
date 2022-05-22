h, m = map(int,input().split())
t = int(input())

if (t + m) >= 60:
    h += (t + m) // 60
    m = (t + m) % 60
    if h >= 24 :
        h %= 24
else:
    m += t
    
print(h, m)

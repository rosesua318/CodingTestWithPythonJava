a, b, c = map(int, input().split())
d = a + b + c

if d >= 100:
    print("OK")
else:
    if min(a, b, c) == a:
        print("Soongsil")
    elif min(a, b, c) == b:
        print("Korea")
    else:
        print("Hanyang")

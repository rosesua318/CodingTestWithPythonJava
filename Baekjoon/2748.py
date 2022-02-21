f = [0, 1]

def fibo(n) :
    global f
    if n < len(f) :
        return f[n]
    else :
        f.append(fibo(n - 1) + fibo(n - 2))
        return f[n]

print(fibo(int(input())))

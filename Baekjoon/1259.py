while True :
    n = input()
    a = "no"
    
    if n == "0" :
        break
    if n == n[::-1] :
        a = "yes"
    
    print(a)

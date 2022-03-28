a = [0, 0, 0, 0, 0]
 
for i in range(5):
    a[i] = int(input())
    
    if a[i] < 40:
        a[i] = 40
        
n  = sum(a)/5       
print(int(n))

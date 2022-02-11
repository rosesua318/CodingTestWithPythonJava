w = input().lower()
a = list(set(w))
count = list()

for i in a :
    c = w.count(i)
    count.append(c)

if(count.count(max(count)) >= 2) :
    print("?")
else :
    print(a[count.index(max(count))].upper())

n=int(input("enter n"))
a=[]
for i in range(0,n):
    a.append(input())
for i in range(0,n):
    minval=min(a[i:])
    minind=a.index(minval)
    a[i],a[minind]=a[minind],a[i]
print(a)
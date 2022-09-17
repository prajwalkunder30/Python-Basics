list=[]
print("enter n:")
n=int(input())
print("enter elements")
for i in range(n):
    list.append(int(input()))
list.sort()
print(list)
print("enter element to search")
key=int(input())
f=0
l=n-1
mid=(f+l)//2
Found=False
c=1
while(f<=l and not Found):
    if(list[mid]==key):
        c=0
        print("search successful")
        break
    elif(list[mid]<key):
        f=mid+1
    else:
        l=mid-1
    mid=(f+l)//2

if(c==1):
    print("search unsuccessful")
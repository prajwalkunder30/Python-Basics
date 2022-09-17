row=int(input("enter no of rows"))
c=1
temp=1+(row-1)*2
for i in range(1,row+1):
    for j in range(1,c+1):
        print(" ",end="")
    for k in range(temp,0,-1):
        print(i,end="")
    c=c+1
    temp=temp-2
    print()


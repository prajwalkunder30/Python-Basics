for i in range(0,4):
    for j in range(0,7):
        if(i==3 and (j==0 or j==6)):
            print(4,end=" ")
        elif((i==2 and (j==1 or j==5)) or (i==3 and (j==1 or j==5) )):
            print(3,end=" ")
        elif((i==2 and (j==2 or j==4)) or (i==3 and (j==2 or j==4) ) or (i==1 and (j==2 or j==4))):
            print(2,end=" ")
        elif(j==3 and(i==0 or i==1 or i==2 or i==3)):
            print(1,end=" ")
        else:
            print(end="  ")
    print()
print(3//2)
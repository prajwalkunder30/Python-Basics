n=int(input("enter number"))
sum=0
temp=n
d=0
while(n>0):
    r=n%10
    sum=sum*10+r
    n=n//10
if(sum==temp):

    c=0
else:
    c=1
    print("no is not a palindromic prime number")
while True:
    if(c==0):
        for i in range(1,temp+1):
            if(temp%i==0):
                d=d+1
        if(d==2):
            print("No is palindromic prime number")
        else:
            print("no is not a palindromic prime number")

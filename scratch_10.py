print("No of apples Harry has got")
n=int(input())
print("enter mx and mn range")
mx=int(input())
mn=int(input())
if mx>mn:
    print("Not valid")
    exit()
for i in range(mx,mn+1):
    if n%i==0:
        print(f"{i} is a divisor of {n}")

    else:
        print(f"{i} is not a divisor of {n}")




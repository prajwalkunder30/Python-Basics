from fractions import math
n1=int(input("enter first no"))
n2=int(input("enter second no"))
if math.gcd(n1,n2)==1:
    print(n1,"and",n2,"are co prime")
else:
    print(n1,"and",n2,"are not co prime")
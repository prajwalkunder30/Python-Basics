num=int(input("enter n"))
k=15
for i in range(num):
    val=k-i
    dec=num-1
    for j in range(i+1):
        print(format(val,"<4"),end="")
        val=val+dec
        dec=dec-1
    print()
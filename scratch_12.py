print("INPUT A LIST")
print("enter n for list")
n=int(input())
list=[]
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
print("INBUILT METHOD OF PYTHON TO REVERSE")
list.reverse()
print(list)
print("SLICING TRICK ")
list[::-1]
print(list)
print("Swapping method")
temp=list[0]
list[0]=list[n-i]
list[n-i]=temp


print(list)
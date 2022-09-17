n = int(input("Enter the number of elements in the array (2-200,000):"))
a = [int(x) for x in input("Enter all numbers of the sequence with only non-negative intergers not exceeding 100,000:").split()]
c = list()

for i in range(0,n):
    for j in range (1,n):
        if a[i] != a[j]:
            m = a[i]*a[j]
            c.append(m)
        else:
            continue
print(max(c))
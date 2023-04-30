def compute(n):
    l = []
    for i in range(1,n):
        l.append((i,i**2,i**3))
    return l
n = int(input("Enter the range of number:"))
print(compute(n))
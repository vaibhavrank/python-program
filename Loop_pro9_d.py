n = int(input("enter a range you want to reverse a number:"))
l=[]
for i in range(n+1):
    l.append(n-i)

for item in l:
    print(item)
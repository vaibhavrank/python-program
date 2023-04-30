a = int(input())
b = int(input())
c = int(input())
f=[a,b,c]
for i in f:
    if i<=39 and i>0:
        print("f")
    elif i<56 and i>40:
        print("u")
    elif i<100 and i>56:
        print("g")
    else:
        print("NA")

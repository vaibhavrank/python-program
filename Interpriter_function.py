def bbonaci(n):
    print("bbonacci series upto ",n)
    a,b=0,1
    while a<n:
        print(a,end=",")
        a,b=b,a+b
    print()


bbonaci(100)
f=bbonaci#here you can see a function is directely pass away to the variable
f(100)
print(f(100))#it wil gives you none because f() is functione without return value




def ram(n=59):#here n=59 is default argumet ,if user not passed any argument then fun. considers default argument as actual argument
    result = []
    a,b= 0,1
    while a<n:
        result.append(a)
        a,b=b , a+b
    return result

k=[]
k.join("we")
print(k)

print(ram())
import math
def f(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else :
        return n*f(n-1)

n =  int(input())
r = int(input())
print("nPr:",(f(n)/f(n-r)))
print("nCr:",((f(n)/(f(r)*f(n-r)))))
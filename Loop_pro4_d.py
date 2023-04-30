# # # pallindrome number
n=int(input("Enetr any number:"))\


num=n
r=0
while num>0:
    digit=num%10
    r = r*10 + digit
    num=num//10

if n==r:
    print("Given number is pallindrome number")
else:
    print("given is not pallindrome")


# # # armstrong
a= int(input("enter a number:"))
c=a

b=0
while a>0:
    f=a%10
    b+=f**3
    a=a//10


    if c==b:
        print("bvsjkaafj")


# Perfect number, a positive integer that is equal to the sum of its proper divisors.

g= (input())
sum =0
for j in range(1,g):
    if (g%j==0):
        sum += j

if sum == g:
    print("yes this is perfect!!!")
else:
    print("jjdghdshaf")



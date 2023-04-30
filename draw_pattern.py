# to draw pattern like thisn
#  *
# ***
#*****
n=int(input("enter the value of n"))
for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(n-i-1))
        
        
#to draw a pattern like this
#*
#**
#***
for i in range(n):
    print("*"*(i+1))
# to draw pattern like this
#* * *
#*   *
#* * *
for i in range(n):
    if i==0:
        print("*"*n)
    elif i==(n-1):
        print("*"*n)
    else:
        print("*"," ","*")
    

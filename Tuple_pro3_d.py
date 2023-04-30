# from datetime import datetime



d1= int(input("enter date 1 day :"))
d2= int(input("enter date 2 day :"))
m1 = int(input("enter date 1 month:"))
m2 = int(input("enter date 2 month:"))
y1 = int(input("ener date 1 year:"))
y2 = int(input("ener date 2 year:"))


# date=[d1,m1,y1]

# DATE = [d2,m2,y2]

# delta = [ datetime.date(d1,m1,y1)-datetime.date(d2,m2,y2)]
# print(delta)
import datetime

# A = ((DD,MM,YYYY), (DD,MM,YYYY))

A = ((d1,m1,y1), (d2,m2,y2))

delta = (
    datetime.date(A[1][2],A[1][1],A[1][0])-
    datetime.date(A[0][2],A[0][1],A[0][0])
)
print(delta)
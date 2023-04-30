import random

l = []
m = []
n = []
for i in range(5):
    l.append(random.randint(1,100))

for j in range(4):
    m.append(  random.randint(0,100))

print(l)
print(m)
l[2] = m

print(l)

#you can flattern your list using four different method
#first method
lol = [[1,2,6,51],[4,8,9],[4,5,6,8]]#all should be a sublist
l1=[item for sublist in lol for item in sublist]
print(l1)

#second method
flatlist = []
for sublist in lol:
    flatlist += sublist
print(flatlist)

#third method
from itertools import chain

fl=list(chain(*lol))
print(fl)

#fourth method
def flatternlist(listoflist,flatlist = []):
    if not listoflist:
        return flatlist
    else:
        for item in listoflist:
            if type(item)==list:
                flatternlist(item,flatlist)
            else:
                flatlist.append(item)

    return flatlist
flatlist = flatternlist(l)
print(flatlist)
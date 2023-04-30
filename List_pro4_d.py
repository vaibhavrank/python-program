import random as e
l = []
m = []
n = []
for i in range(30):
    l.append(e.randint(-100,100))
for j in l:
    if j<0:
        m.append(j)
    elif j>0:
        n.append(j)
    else:
        m.append(j)

print(l,m,n)
import random as r
l = []
for i in range(51):
    l.append(r.randint(0,31))
print(l)

l = list(set(l))#remove all duplicate value from list
print(l)


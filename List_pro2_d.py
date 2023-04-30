import random as rn
l = []
for i in range(20):
    l.append(rn.randint(0,100))
print(l)
n = int(input())
print("ocuurance is:",l.count(n))
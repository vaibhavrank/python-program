import random as rd
set_number = set()

for i in range(21):
    set_number.add(rd.randint(15,45))
greater_number = set()
count= 0
print(set_number)
for i in set_number:
    if i<=30:
        count+=1
   
    if i<35:
        greater_number.add(i)
    else:
        pass

print(greater_number)
print(count)
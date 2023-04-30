#set
a ={1,3,4,2,1}
print(type(a))
print(a)
#if i want to make an empty set you have to follow this syntax

b ={3,3,89,6,5,4,4}
print(type(b))
b.add("raghav")#you cant add a list or dictioanary in set
#you can add a tupple in a set
print(len(b))# prints the lengthb of th e set
b.remove(3)#removes 3 from the set
# print(remove(34)#throws an arror bcause there is no such element in set
print(a.pop())#removes a random element and returns that element
print(a)
#print(b.clear())#empties the set
print(b.union({b,a}))

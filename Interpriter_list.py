square=[1,2,3,4,5,6,7,8,9,10]
print(square)
print(square[2])#you can access elements of the list by indexing
print([1,2,3,4,5,6,6]+square)


#you can change list elements value by indexing
square[5]=456
print(square)

#you can append any element by list.append(value)
square.append(2266)
print(square)
square.append(7**3)
print(square)



letter = ['j','a','y','s','h','r','e','e','r','a','m']

#you have to be ncarefull with indexing[m:n] because it will consider n-1 limit 

print(letter[0:3])

#you can remove and replace some part of list by following

letter[0:3]=[]
print(letter)
letter[0:3]=['j','a','y']
print(letter)

#python supports nested list
s=[letter,square]
print(s)
#unlock the nested list by module or for loop
#show List_unpack.py program

# remove some part ofrom a single string

Ram  = input("enter a string: ")

Shyam = input("ENter a second string: ")
# print(Shyam.replace(Ram,''))

if Ram in Shyam:
    print(Shyam.replace(Ram,''))
    
elif Shyam in Ram:
    print(Ram.replace(Shyam,''))
    
else:
    print("There is not anyb sunb string is found")


#now let take a string
ram = 'Jay Shree Ram'
print(ram.replace('Jay Shree',''))

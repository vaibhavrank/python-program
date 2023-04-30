for i in range(9):
    if i==5:
       break
    print(i)
else:
     print("this is inside else of for")
     """#if loop will terminates successfully only then else condition will exicute that means if we
       want to check wether the loop exicuted successfully or not the we use this else syntax"""



print("\n")
for i in range(9):
    if i==5:
       continue
    print(i)
else:
     print("this is inside else of for")

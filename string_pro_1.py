#count hoow many vowels in the string


ram=input("enter a string:")
count=0
for i in ram:
    if((i=='a')or(i=='i')or(i=='o')or(i=='e')or(i=='u')):
        count+=1


print(len(ram))
print("The number of vowels in given striing is",count)


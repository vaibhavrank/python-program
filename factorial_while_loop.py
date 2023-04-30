#factorial using while loop
num =int(input("enter a term of factorial:"))
factorial=1
i=1
while i<=num:
    factorial = factorial*i
    i=i+1
print(factorial)

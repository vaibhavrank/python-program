s=(input("input any string:"))
bount=0
count=0
for i in range(0,len(s)-1):
    if ord(s[i])<=90 and ord(s[i])>=65:
        count+=1
    elif ord(s[i])>=97 and ord(s[i])<=122:
        bount+=1
    print(ord(s[i]))
print(f" Capital letter: {count} small letter: {bount}")
print(ord('.'))
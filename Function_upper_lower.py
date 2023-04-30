s = 'ddguguyVVVVV'
def count_upper_lower(s):
    c,l=0,0
    for i in s:
        if i.isupper():
            c+=1
        elif i.islower():
            l+=1
    return {'uppercase':c,'lower case':l}
print(count_upper_lower(s))
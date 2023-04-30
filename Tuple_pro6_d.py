#del and mmodify a tuple
a=('dhjg','jgff','jkdnk','whdgfgwfg')
b = ()
for i in a:
    if i==1:
        i=None
    else:
        b = b + tuple(i)
print(b)


#elelment of tuple can be deleted only whole tuple is deleted
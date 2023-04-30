import os,sys
fr = open("file.txt",'r')


cl=1
cw=cc=0

for i in fr:
    word = i.split()
    print(word)
    cl = cl 
    cw = cw + len(word)
    cc = cc +len(i)

print(cl    ,cw      ,cc)
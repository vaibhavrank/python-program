import os,sys
fw = input("input file name : ")
if os.path.isfile(fw):
    f = open(fw,'r')
else:
    print("file does not exist")
    sys.exit()


ch = f.read(1)
while ch!="":
    print(ch,end="")
    ch= f.read(1)
f.close()
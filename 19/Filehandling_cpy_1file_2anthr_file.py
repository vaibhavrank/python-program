# import os,sys
flname = input("Enter the file nsame you want to cpy")
# if os.path.isfile(flname):
f  = open(flname,"r+")
# else:
    # print("file does not exist")
    # sys.exit()

fwnm = input("Enter the file namr you want to paste:")
fw = open(fwnm,"w")




#if you want  to check that file is exist or not for this you can imort module  "os","sys" 



ch = f.read()
while ch!= "":
    fw.write(ch)
    print(ch,end="",file=fw)
    ch = f.read()

f.close()
fw.close()
print("thid is")

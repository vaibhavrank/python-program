# tpl1 = [1,5,3,4,5,5,5,5,5]
# f = open("v.txt","w")
# f.write(str(tpl1))
# f.close()
# This program creates a file on the hard disk and writes the content within a file.

flname = input("Enter a File Name to write the content.")

f = open(flname,'a+')
ch = input("Enter text that you want to write in a file. At the end enter ~ character.")

while ch != '~':

    f.write(ch)

    ch = input()

f.write('\n')

f.close()

print(flname, "has been succssefully created on the hard disk.")
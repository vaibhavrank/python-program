# # #conver whole sreing into upper lower amd toggle case
# # Ram = input("Enter a string : ")


# # def convert_upper(str):
# #     for i in str:
# #         if str[i]<=90:
# #            str.replace(str[i],str[i]+32)
# #     return str



# # print(convert_upper)
# str=input("Enter the String(Lower case):")
# i=0
# ch=''
# #convert capital letter string to small letter string
# while len(str)>i:
#     if str[i]>='a' and str[i]<='z' :
#         ch+=chr(ord(str[i])-32)
#     else:
#         ch += chr(ord(str[i]))
#     i+=1
# print("Lower case String is:", ch)

ram = input("emter the string:  ")
  


i = 0
ch = ''
 
while i<len(ram):

    if ord(ram[i])<=97 and ord(ram[i])>=65:
        ch+=chr(ord(ram[i])+32)
    else:
        ch+=chr(ord(ram[i]))
    i+=1


print(ch)

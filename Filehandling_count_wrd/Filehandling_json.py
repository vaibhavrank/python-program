import json

f = open('Sampledata','w+')

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]

json.dump(lst,f)

f.seek(0)
# ch = f.read()
# while ch!="":
#     print(ch,end="")
#     ch = f.read()

inlst = json.load(f)

print(inlst)

f.close()
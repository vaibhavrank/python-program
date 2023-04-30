import json

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]

tpl = ('Darshit','18/02/1972', 'O+ve')

dct = { 'Darshit': 52, 'Ragi' : 49 }

str1 = json.dumps(lst)

str2 = json.dumps(tpl)

str3 = json.dumps(dct)

l = json.dumps(lst)

t = tuple(json.loads(str2))

d = json.loads(str3)

print (l, t, d) 
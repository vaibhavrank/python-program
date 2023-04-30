f = open('a.dat', 'wb+')

d = b'\xee\x86\xaa'
f.write(d)

f.seek(512,0)
f.seek(0,2)
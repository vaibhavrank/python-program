import os, time, shutil

import shutil

print ("OS Name:", os.name)

print (os.getcwd())

print (os.listdir('.'))

print (os.listdir('..'))

if os.path.exists('mydir'):

    print ('Mydir already exists.')

else:

    os.mkdir('mydir')

os.chdir('mydir')

if os.path.exists('.\\dir1\\dir2\\dir3'):

    os.chdir('.\\dir1\\dir2\\dir3')

else:

    os.makedirs('.\\dir1\\dir2\\dir3')

f = open('myfile.txt','w')

f.write('Hi, learn Python file handling in simple manners.\n')

f.close()

stats = os.stat('myfile.txt')

print('Size = ',stats.st_size)

os.rename('myfile.txt','yourfile.txt')

shutil.copyfile('yourfile.txt','ourfile.txt')

os.remove('yourfile.txt')

curpath = os.path.abspath('.')

os.path.join(curpath,'yourfile.txt')

if os.path.isfile(curpath):

    print('Yourfile file does exist.')

else:

    print('Yourfile file doesn\'t exist.')

file = 'ourfile.txt'

print(file)

created = os.path.getctime(file)

modified = os.path.getmtime(file)

accessed = os.path.getatime(file)

print ('Date created:' + time.ctime(created))

print ('Date modified:' + time.ctime(modified))

print ('Date accessed:' + time.ctime(accessed))
set1 = ('asmita','apple','ball','answer','big bull','africa','american','baa')
set2 = set()
set3 = set()

for item in set1:
    if item.startswith('a'):
        set2.add(item)
    elif item.startswith('b'):
        set3.add(item)
    else:
        pass
print("words which starts with 'a':",set2)
print("word which starts with 'b':",set3)
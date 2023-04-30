#Remove empty tuple(s) from the list of tuples.

l=[(),('dfjag'),(),('hjqbfj'),()]
m= []

for i in l:
    if not i:
        i=None
    else:
        m.append(i)


print(m)



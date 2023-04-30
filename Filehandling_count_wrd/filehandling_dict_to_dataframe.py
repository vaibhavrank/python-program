import pandas as pd


dic1 = {'name':['vaibhav','viraj','maulik'],
        'roll no':[183,184,186],
        'maths':[99,100,100],
        'physics':[50,86,90],
        'chemistry':[100,100,100]
        }
df = pd.DataFrame(dic1)
# df.to_csv("python.xlsx",index=False)
print(df)
print('\n')
df.to_csv('friend.csv',index=False)
print(df)
print('\n')
print(df.head(2))
print('\n')
print(df.tail(2))
print('\n')
print(df['name'][2])
# d = df.to_excel('python.xlsx')
# print(d)
D = df.index =[1,2,3]
print('\n')
print(df)
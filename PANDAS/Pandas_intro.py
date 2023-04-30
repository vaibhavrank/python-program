import pandas as pd
data = {
    'name':[1,2,3,3,3,5],
    'data':[45,65,89,89,63,56]
       }
df = pd.DataFrame(data)
print(df)
# print(pd.describe_option(df))
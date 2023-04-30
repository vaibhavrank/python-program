# create a list with name
name = ['grapse', 'mango', 'gvava', 'apple', 'banana']
price = [100,100,40,50,30]
# zip the two lists using iter() function
data = sorted([list(zip(price,name))],reverse=True)  
# display data
print(data)
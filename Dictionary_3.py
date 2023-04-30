# Create two dictionaries – one containing grocery items and their prices and 
# another containing grocery items and quantity purchased.
#  By using the values from these two dictionaries compute the total bill


price = {'Banana':50,
        'wheat': 100,
        'chaval':100}
qunty = {'Banana':5,
         'wheat':89,
         'chaval':100}
sum = 0
for item in price:
    sum += price[item] * qunty[item] 

print(sum)
# print(5*50+100*89+100*100)

# for item in price:
#     print(price[item])
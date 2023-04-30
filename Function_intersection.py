def isintersection(s1,s2):
    s1 = set(s1)
    s2 = set(s2)
    intersection = s1.intersection(s2)

    result = list(intersection)
    return result
l1 =['sdsdbfjb','dfdjwf','list','idfhwhf','jfljlf']
l2 = ['fkdfhwfh','fhhfwh','list','fgewjfg','ndkfhj']
l3 = ["vaibhav"]
l4 = ["vabhav"]

print(isintersection(l3,l4))

print(isintersection(l1,l2))
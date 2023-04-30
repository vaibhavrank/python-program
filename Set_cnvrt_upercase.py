# str = 'fdlkghowjfquigfowrjgerhffiqfhwrgj'
# lst = list(str.upper())
# SET = set(lst)
# print(SET)

list1 = ['knwbw','fhvh','wlfjwfh','miwdhw','hfwihfi','fhghwwh','ffjowjggjr9guug43']
uppercase_set = set()

def cnvrt_upper_and_stor_in_set(word_list):
    for i in word_list:
        uppercase = i.upper()
        uppercase_set.add(uppercase)

    return uppercase_set
uppercase_set = cnvrt_upper_and_stor_in_set(list1)

print(uppercase_set)
print(list1)
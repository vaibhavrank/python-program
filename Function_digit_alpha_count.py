def count_digit_alpha(s):
    count,count1 = 0,0
    for i in s:
        if i.isalpha():
            count += 1
        elif i.isdigit():
            count1 += 1
        else:
            pass
    return {'number of digit':count1,'number of alphabet':count}


print(count_digit_alpha("dfuhfhfsdj12354     "))
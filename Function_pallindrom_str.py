def ispallindrome(S):

    f = S[::-1]
    if S==f:
        print("Yes!!,this string is pallindrome.")
    else:
        print("No,This is not!!")


s = "vaibhav"
d = "vavavav"
ispallindrome(s) 
ispallindrome(d)       


# print(f,s)
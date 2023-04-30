def ispangram(s):
    s =s.lower()
    s= s.replace(" ","")
    
    set1 = set(s)
    # print(sorted(set1))
    if len(set1)==26:
        return True
    else:
        return False
        # print("given sentence is not panigram")

if ispangram("The quick brown fox jumps over the lazy dog"):
    print(True)
else:
    print(False)
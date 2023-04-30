"""Write a program that defines a function convert() that receives 
   a string containing a sequence of whitespace separated words 
   and returns a string after removing all duplicate words and 
   sorting them alphanumericall"""
def convert(s):
    s = s.upper()
    s = s.replace(" ","")
    # s = s.sort()
    set1 = set(s)
    print(sorted(set1,reverse = True))

convert("bskaf nsff  13244314361 21474 461 uy361 hfakf mhkhf khf HYF FF")
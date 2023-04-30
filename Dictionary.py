myDict = {
    "vaibhav":"for a singlae line",
    "number":[1,2,3]
     }
print(myDict['number'])
myandict = {
    "vaibhav2":"for the multiple setense",
    "sfkj":"second line",
    "dictinandict":{'andict':'dict into another dict attention'}
    }#here both of inverted single and double comma is considered
print(myandict['vaibhav2'])
print(myandict['dictinandict']['andict'])
#methods of dictionary
print(list(myandict.keys())) #to prints keys of the dictioanary
print(list(myandict.values()))# to prints values of the dictioanary
print(myandict.values()) #to print values of the keays without listing
print(myandict.items()) #to print the (key,value) for all contents of the dictionary
print(myandict)
updatedict = {
    "lovis":"vaibhav"
    }               #to update my dictionary0 to update exist key or to enter new leys
myDict.update(updatedict)
print(myDict)
print(myDict.get("vaibhav2"))'''#if thre is not exist given key in the dictionary then
then .get function returns none inspiyte of key arror'''


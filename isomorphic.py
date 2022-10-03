def isomorphic(str1,str2):
    dict_str1={}
    dict_str2={}
    for i,value in enumerate(str1):
        dict_str1[value]=dict_str1.get(value,[])+[i]
    for j,value in enumerate(str2):
        dict_str2[value]=dict_str1.get(value,[])+[j]
    if sorted(dict_str1.value())==sorted(dict_str2.value()):
        return true
    else:
        return false
str1=input("enter the string:")
str2=input("enter the string:")
print(isomorphic(str1,str2))

newlist = [1,2,3,"d",4,5,'a']
num, char = [],[]
for i in newlist:
    if isinstance(i,int):
        num.append(i)
    elif isinstance(i,str):
        char.append(i)
print(
    "The numbers are: ",num,
    "The Strings are: ",char
)
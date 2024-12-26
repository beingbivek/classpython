newlist = [1,2,3,"d",4,5,'a']
num, char = [],[]
for i in newlist:
    if isinstance(i,int):
        print(i," is an Integer")
    elif isinstance(i,str):
        print(i," is a String")
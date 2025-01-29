lst = [1,2,3,4]
new_list = []
# [1,'a',2,4]

def addtolist(i):
    new_list.append(i)

for i in lst:
    if i == 2:
        addtolist('a')
    elif i == 3:
        addtolist(2)
    else:
        addtolist(i)

print(new_list)
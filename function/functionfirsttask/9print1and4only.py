lst = [1,2,3,4]

def printval(i):
    print(i)

for i in lst:
    if i == 2 or i == 3:
        continue
    else:
        printval(i)
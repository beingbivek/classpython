newlist = [1,'a','c',2,3,4]
for l in newlist:
    try:
        print(int(l))
    except:
        continue

# 2nd method
for n in newlist:
    if isinstance(n,int):
        print(n)
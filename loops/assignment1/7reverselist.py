oldlist = [1,'a','2323','adsaf',123123]
reversedlist = []
for i in range(len(oldlist)-1,-1,-1):
    reversedlist.append(oldlist[i])
print(f'Original list is: {oldlist}')
print(f'Reversed list is: {reversedlist}')

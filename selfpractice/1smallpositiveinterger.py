lst = [3,4,-1,1]
smallest = max(lst)
for i in lst:
    if i >= 0 and smallest > i:
        smallest = i
print('The positive smallest number is: ',smallest)
numlist = [1,2,4,342,234556,67535,1234,1243,3564,34556,56,244,235,345,7235,65,856,6]
evencount = oddcount = i = 0
while i < len(numlist):
    if numlist[i] % 2 == 0:
        evencount += 1
    else:
        oddcount += 1
    i += 1
print('The number of even numbers are',evencount,'and odd numbers are',oddcount)

a = [1,2,3,4,5]
even,odd = [],[]
i = 0
while i < len(a):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
    i += 1
print('The even numbers are: ',even,'and the odd numbers are: ',odd)
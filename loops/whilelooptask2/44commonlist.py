a = [1,2,3,4,5]
b = [3,4,5,6,7]
i = 0
while i < len(a):
    check = False
    j = 0
    while j < len(b):
        if a[i] == b[j]:
            check = True
            break
        j += 1
    if check == True:
        print(a[i])
    i += 1
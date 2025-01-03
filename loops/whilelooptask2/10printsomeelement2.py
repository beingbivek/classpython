a = [1,2,3,4]
i = 0
while i < len(a):
    if a[i] == 3:
        i += 1
        continue
    print(a[i])
    i += 1
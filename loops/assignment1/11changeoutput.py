old = [1,2,3,4]
new = []
for i in old:
    if i == 2:
        i = "a"
    elif i == 3:
        i = 2
    new.append(i)
print(new)
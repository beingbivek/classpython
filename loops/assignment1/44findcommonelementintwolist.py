a = [1,2,3,4,5]
b = [3,4,5,6,7]
c = []

for i in a:
    for j in b:
        if i == j:
            c.append(i)

print("The common elements are: ",c)
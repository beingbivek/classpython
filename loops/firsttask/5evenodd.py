even,odd = [],[]
for i in range(20):
    if len(even) <= 10 and len(odd) <= 10:
        if i % 2 == 0:
            even.append(i)  
        else:
            odd.append(i)
    else:
        break

# a.
print(even)
# b.
print(odd)
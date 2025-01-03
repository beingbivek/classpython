lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
p_list = []
i = 0
while i < len(lst1):
    if lst1[i] > 0:
        p_list.append(lst1[i])
    i += 1
print(p_list)
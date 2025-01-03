a = [1,2,3,4]
expected_list = []
i = 0
while i < len(a):
    if a[i] == 2:
        expected_list.append("a")
    elif a[i] == 3:
        expected_list.append(2)
    else:
        expected_list.append(a[i])
    i += 1
print(expected_list)
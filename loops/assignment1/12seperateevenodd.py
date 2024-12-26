all_list = [1,2,3,4,5]
even, odd = [],[]
for i in all_list:
    if i % 2 == 0:
        # print(even,"o")
        even.append(i)
    else:
        # print(odd,"l")
        odd.append(i)
else:
    print("Odd list is: ",odd,"and even list is:",even)
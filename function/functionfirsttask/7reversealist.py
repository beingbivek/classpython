lst = [1,2,3,4,5]

def reverselist(o_list):
    rev_list = []
    for i in range(len(lst)-1,-1,-1):
        rev_list.append(o_list[i])
    return rev_list

print(reverselist(lst))
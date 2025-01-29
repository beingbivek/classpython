lst = [1,2,3,4]

def updatelist(o_list):
    u_list = []
    for i in range(len(o_list)):
        u_list.append(o_list[i]+1)
    return u_list

print(lst,updatelist(lst))
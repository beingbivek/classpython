given_list = [1,2,3,'d',6.43,4,5,'a',1.0001,'asd',12]
type_list = []
i = 0
while i < len(given_list):
    value = given_list[i]
    if isinstance(value,int):
        type_list.append("int")
    elif isinstance(value,str):
        type_list.append("str")
    elif isinstance(value,float):
        type_list.append("float")
    i += 1
print(
    'The type list is: ', type_list,
)
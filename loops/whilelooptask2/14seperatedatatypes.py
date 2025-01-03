given_list = [1,2,3,'d',6.43,4,5,'a',1.0001,'asd',12]
int_list,str_list,float_list = [],[],[]
i = 0
while i < len(given_list):
    value = given_list[i]
    if isinstance(value,int):
        int_list.append(value)
    elif isinstance(value,str):
        str_list.append(value)
    elif isinstance(value,float):
        float_list.append(value)
    i += 1
print(
    'The integer list is: ', int_list,
    'The string list is: ', str_list,
    'The float list is: ', float_list,
    sep='\n'
)
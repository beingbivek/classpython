given_list = [1,2,3,'d',4,5,'a',1.0001]
i = 0
while i < len(given_list):
    # print(type(given_list[i]))
    value = given_list[i]
    if isinstance(value,int):
        print(value,'is an integer')
    elif isinstance(value,str):
        print(value,'is a string')
    elif isinstance(value,float):
        print(value,'is a float')
    i += 1
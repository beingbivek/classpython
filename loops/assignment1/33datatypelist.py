lists,datatype = [],[]
user_input = int(input("How many variables would you add: "))
for i in range(user_input):
    new_var = input(f"Enter {i+1} variable(float, string, int, dict.etc.): ")
    lists.append(new_var)

for data in lists:
    datatype.append(type(data))
print(datatype)
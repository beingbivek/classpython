# a='softwarica'
# for i in a:
#     print(i)

# for i in reversed(a):
#     print(i)

# for i in range(len(a)-1,-1):
#     print(a[i])

# for i in range(len(a)):
#     print(a[i],"=",i)

# user_input = int(input("Enter a number for its multiplication table : "))
# for i in range(1,11):
#     print(f'{user_input} * {i} = {user_input * i}')

# print("\n")

# for i in range(10,0,-1):
    # print(f'{user_input} * {i} = {user_input * i}')


numbers = []
user_input = int(input("How many number would you add: "))
for i in range(user_input):
    new_num = int(input(f"Enter {i+1} number: "))
    numbers.append(new_num)
sum,product = 0,1
# print(numbers)
for n in numbers:
    sum += n
    product *= n
print(f'Sum is {sum} and Product is {product}')

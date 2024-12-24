numbers = []
user_input = int(input("How many number would you add: "))
for i in range(user_input):
    new_num = int(input(f"Enter {i+1} number: "))
    numbers.append(new_num)

mul = 1
for num in numbers:
    mul *= num
print(f"Multiplication of the list {numbers} is: {mul}")
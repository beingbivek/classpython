numbers = []
user_input = int(input("How many number would you add: "))
for i in range(user_input):
    new_num = int(input(f"Enter {i+1} number: "))
    numbers.append(new_num)

sum = 0
for num in numbers:
    sum += num
print(f"Sum of the list {numbers} is: {sum}")
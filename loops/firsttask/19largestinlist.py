numbers = []
user_input = int(input("How many number would you add: "))
for i in range(user_input):
    new_num = int(input(f"Enter {i+1} number: "))
    numbers.append(new_num)

largest_num = 0
for num in numbers:
    if num > largest_num:
        largest_num = num

print(f"The largest number is: {largest_num}")
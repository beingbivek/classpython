numbers = []
user_input = int(input("How many number would you add: "))
for i in range(user_input):
    new_num = int(input(f"Enter {i+1} number: "))
    numbers.append(new_num)

for num in numbers:
    if num % 2 != 0:
        print(num)
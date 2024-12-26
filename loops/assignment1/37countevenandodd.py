numbers = []
user_input = int(input("How many numbers would you add: "))
for i in range(user_input):
    new_var = input(f"Enter {i+1} Number: ")
    numbers.append(new_var)

even = odd = 0
for number in numbers:
    if int(number) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Total even no are:",even,",and odd no. are:",odd)
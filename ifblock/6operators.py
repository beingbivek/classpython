first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))
operator = input("Enter operator (+,-,/,*): ")

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "/":
    print(first_number / second_number)
elif operator == "*":
    print(first_number * second_number)
else:
    print("Invalid operator.")
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
    print(f"Your Answer is: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"Your Answer is: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Your Answer is: {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Your Answer is: {result}")
    else:
        print("Division by zero is Invalid.")
else:
    print("Invalid operator!")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Sum: ", num1 + num2)
elif num1 % 2 == 0 or num2 % 2 == 0:
    print("Difference: ", num1 - num2)
else:
    print("Product: ", num1 * num2)
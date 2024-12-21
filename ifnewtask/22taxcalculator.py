age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
income = float(input("Enter your income: "))

if age >= 18 and age < 60:
    if gender == 'M':
        if income > 1000000:
            tax = income * 0.30
        elif 500000 < income <= 1000000:
            tax = income * 0.20
        else:
            tax = income * 0.10
    elif gender == 'F':
        if income > 1000000:
            tax = income * 0.25
        elif 500000 < income <= 1000000:
            tax = income * 0.15
        else:
            tax = income * 0.05
elif age >= 60:
    if income > 1000000:
        tax = income * 0.20
    else:
        tax = income * 0.10
else:
    tax = 0

print("Your tax amount is:", tax)

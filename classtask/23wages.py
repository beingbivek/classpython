age = int(input("Enter your age: "))
gender = input("Enter your Gender(M/F): ").lower()
days = int(input("Enter no. of working day\'s: "))
g = 1
if age >= 18 and age < 30:
    if gender == 'm':
        wage = days * 700
    elif gender == 'f':
        wage = days * 750
    else:
        g = 2
elif age >= 30 and age <= 40:
    if gender == 'm':
        wage = days * 800
    elif gender == 'f':
        wage = days * 850
    else:
        g = 2
else:
    g = 0

if g == 2:
    print("Invalid Gender!")
elif g == 0:
    print(f"{age} years old can't work in the company!")
else:
    print(f"Your Total wage is {wage}")
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
mark = int(input("Enter your academic mark (out of 100): "))
nos = "No Scholarship"
if 18 <= age <= 25:
    if gender == 'M':
        if mark >= 85:
            print("Full Scholarship")
        elif mark >= 70:
            print("Partial Scholarship")
        else:
            print(nos)
    elif gender == 'F':
        if mark >= 80:
            print("Full Scholarship")
        elif mark >= 65:
            print("Partial Scholarship")
        else:
            print(nos)
else:
    print("Not eligible")

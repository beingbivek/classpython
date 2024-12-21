age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
experience = int(input("Enter your experience in years: "))

if 21 <= age <= 35:
    if gender == 'M':
        if experience >= 5:
            role = "Senior Developer"
        else:
            role = "Junior Developer"
    elif gender == 'F':
        if experience >= 5:
            role = "Senior Analyst"
        else:
            role = "Junior Analyst"
elif age > 35:
    role = "Manager Role"
else:
    role = "Not eligible based on age"

print("Assigned role:", role)

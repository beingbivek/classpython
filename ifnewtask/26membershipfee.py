age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
membership_type = input("Enter the membership type (Monthly/Yearly): ").capitalize()

if 18 <= age < 30:
    if gender == 'M':
        if membership_type == "Monthly":
            fee = 50
        elif membership_type == "Yearly":
            fee = 500
    elif gender == 'F':
        if membership_type == "Monthly":
            fee = 45
        elif membership_type == "Yearly":
            fee = 450
elif 30 <= age <= 50:
    if membership_type == "Monthly":
        fee = 60
    elif membership_type == "Yearly":
        fee = 600
elif age > 50:
    if membership_type == "Monthly":
        fee = 40
    elif membership_type == "Yearly":
        fee = 400
else:
    fee = 1

if fee == 1:
    print("Children and teenagers can't have memberships.")
else:
    print("Membership fee:", fee)

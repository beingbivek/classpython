age = int(input("Enter the candidate's age: "))
degree = input("Does the candidate have a degree? (yes/no): ").lower()
experience = int(input("Enter the candidate's work experience in years: "))

if age >= 18:
    if degree == "yes":
        if experience > 3:
            print("Highly Eligible")
        elif experience >= 1:
            print("Eligible")
        else:
            print("Under Review")
    else:
        print("Not Eligible due to lack of degree")
else:
    print("Not Eligible due to age")

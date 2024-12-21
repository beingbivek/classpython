salary = int(input("Enter your monthly salary: "))
if salary > 50000:
    print("High Earner")
elif salary <= 50000:
    if salary > 20000:
        print("Mid Earner")
    else:
        print("Low Earner")
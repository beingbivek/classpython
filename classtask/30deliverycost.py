weight = float(input("Enter weight of package in Kg: "))
delivery_type = input("Is the delivery urgent (y/n): ").lower()
status = 0
if weight < 5 and weight > 0:
    cost = 5
elif weight >= 5 and weight <= 20:
    cost = 10
elif weight > 20:
    cost = 20
else:
    status = 1

if (status == 1):
    print("Invalid Weight!")
elif delivery_type == 'y':
    print(f"With urgent delivery, total delivery charge is: {cost + 5}")
else:
    print(f"Total delivery charge is: {cost}")
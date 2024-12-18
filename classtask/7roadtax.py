cost_of_bike = int(input("Enter Cost of bike: "))
if cost_of_bike <= 50000:
    tax = 5
elif cost_of_bike > 100000:
    tax = 15
else:
    tax = 10

print(f"Road TAX for Rs.{cost_of_bike} bike is Rs.{cost_of_bike * (tax/100)}")
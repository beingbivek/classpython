days = int(input("Enter no. of days you need to access library: "))

if days <= 5:
    charge = days * 2
elif days <= 10:
    charge = days * 3
elif days <= 15:
    charge = days * 4
else:
    charge = days * 5

print(f"The charge for library for {days} days is Rs.{charge}")

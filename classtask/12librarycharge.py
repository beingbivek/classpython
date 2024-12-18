days = int(input("Enter no. of days you need to access library: "))

if days <= 5:
    charge = days * 2
elif days <= 10:
    charge = ((days - 5) * 3) + (5 * 2) 
elif days <= 15:
    charge = ((days - 10) * 4) + (5 * 2) + (5 * 3) 
else:
    charge = ((days - 15) * 5) + (5 * 2) + (5 * 3) + (5 * 4)

print(f"The charge for library for {days} days is Rs.{charge}")

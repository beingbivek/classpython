timeperiod = int(input("How many years you have been in the company: "))
salary = int(input("How much is your salary: "))

if timeperiod > 5:
    bonus = salary * 0.05
    print(f"For {timeperiod} years, bonus is Rs.{bonus}")
else:
    print("No bonus.")

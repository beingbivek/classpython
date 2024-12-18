timeperiod = int(input("How many years you have been in the company: "))
salary = int(input("How much is your salary: "))
if timeperiod > 10:
    print(f"For {timeperiod} years, bonus is Rs.{salary * 0.1}")
elif timeperiod >= 6 and timeperiod <= 10:
    print(f"For {timeperiod} years, bonus is Rs.{salary * 0.08}")
elif timeperiod < 6 and timeperiod >= 0:
    print(f"For {timeperiod} years, bonus is Rs.{salary * 0.05}")
else:
    print("Invalid time period!")

percentage = float(input("Enter the percentage: "))

if percentage < 40 and percentage >= 0:
    print("Category: Failed")
elif percentage >= 40 and percentage < 55:
    print("Category: Fair")
elif percentage >= 55 and percentage < 65:
    print("Category: Good")
elif percentage >= 65 and percentage <= 100:
    print("Category: Excellent")
else:
    print("Invalid percentage!")
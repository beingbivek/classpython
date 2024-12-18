weather = input("Enter the weather (sunny/rainy/winter): ").lower()

if weather == "sunny":
    print("It's a great day for outdoor activities like hiking or a picnic!")
elif weather == "rainy":
    user_have = input("Do you have a raincoat or umbrella? (yes/no): ").lower()
    if user_have == "yes":
        print("Visit a nearby mall or museum.")
    else:
        print("It's best to stay home and watch some movies.")
elif weather == "winter":
    snow = input("Is it snowing? (yes/no): ").lower()
    if snow == "yes":
        print("It's best to stay home and watch some movies.")
    else:
        print("Go to a Coffee Shop.")
else:
    print("Invalid weather input!")

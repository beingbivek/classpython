print("Welcome to the Jungle Adventure")
GO = "Game Over!"
invalid = "Invalid Number Inserted!"

print("1. Left\n2. Right")
user_choice = int(input("Choose an option (1/2): "))
if user_choice == 2:
    print(GO)
elif user_choice == 1:
    print("1. Climb a tree\n2. Explore the cave")
    user_choice = int(input("Choose an option (1/2): "))
    if user_choice == 1:
        print(GO)
    elif user_choice == 2:
        print("1. Bear\n2. Tiger\n3. Snake")
        user_choice = int(input("Choose an option (1/2/3): "))
        if user_choice == 1 or user_choice == 2:
            print(GO)
        elif user_choice == 3:
            print("You Win!")
        else:
            print(invalid)
    else:
        print(invalid)
else:
    print(invalid)

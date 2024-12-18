print("Welcome to the Space Mission")
GO = "Game Over!"
invalid = "Invalid Number Inserted!"

user_choice = int(input("1. To the moon\n2. To Mars\nChoose an option (1/2): "))
if user_choice == 2:
    print(GO)
elif user_choice == 1:
    user_choice = int(input("1. Land on the surface\n2. Stay in orbit\nChoose an option (1/2): "))
    if user_choice == 1:
        print(GO)
    elif user_choice == 2:
        user_choice = int(input("1. Alien\n2. Asteroid\n3. Satellite\nChoose an option (1/2/3): "))
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

print("Welcome to the Magic Forest")
GO = "Game Over!"
invalid = "Invalid Number Inserted!"

user_choice = int(input("1. North\n2. South\nChoose an option (1/2): "))
if user_choice == 2:
    print(GO)
elif user_choice == 1:
    user_choice = int(input("1. Cross the river\n2. Follow the path\nChoose an option (1/2): "))
    if user_choice == 1:
        print(GO)
    elif user_choice == 2:
        user_choice = int(input("1. Fairy\n2. Ogre\n3. Elf\nChoose an option (1/2/3): "))
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

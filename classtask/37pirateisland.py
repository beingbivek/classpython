print("Welcome to the Pirate Island")
GO = "Game Over!"
invalid = "Invalid Number Inserted!"

user_choice = int(input("1. Left\n2. Right\nChoose an option (1/2): "))
if user_choice == 2:
    print(GO)
elif user_choice == 1:
    user_choice = int(input("1. Dig for treasure\n2. Sail the ship\nChoose an option (1/2): "))
    if user_choice == 1:
        print(GO)
    elif user_choice == 2:
        user_choice = int(input("1. Shark\n2. Pirate ship\n3. Mermaid\nChoose an option (1/2/3): "))
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

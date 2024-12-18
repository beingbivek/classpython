print("Welcome to the Haunted House")
GO = "Game Over!"
invalid = "Invalid Value Inserted!"

user_choice = input("Do you want to go 'upstairs' or 'downstairs': ").lower()
if user_choice == "downstairs":
    print(GO)
elif user_choice == "upstairs":
    user_choice = input("Do you want to 'enter the room' or 'stay outside': ").lower()
    if user_choice == "enter the room":
        print(GO)
    elif user_choice == "stay outside":
        user_choice = input("Choose between 'ghost', 'vampire', or 'werewolf': ").lower()
        if user_choice == "ghost" or user_choice == "vampire":
            print(GO)
        elif user_choice == "werewolf":
            print("You Win!")
        else:
            print(invalid)
    else:
        print(invalid)
else:
    print(invalid)

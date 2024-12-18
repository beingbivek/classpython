print("Welcome to Treasure Land\nChoose a direction (left/right): ")
GO = "Game Over!"
invalid = "Invalid Value Inserted!"
user_choice = input("Enter Your Direction: ").lower()
if user_choice == "right":
    print(GO)
elif user_choice == "left":
    print("Good, Now do you want to swim or wait: ")
    user_choice = input("Enter your desired activity: ").lower()
    if user_choice == "swim":
        print(GO)
    elif user_choice == "wait":
        print("Great, select a color red, blue or yellow: ")
        user_choice == input("Enter your choice of color: ").lower()
        if user_choice == 'blue' or user_choice == 'red':
            print(GO)
        elif user_choice == 'yellow':
            print("You win!")
        else:
            print(invalid)
    else:
        print(invalid)
else:
    print(invalid)
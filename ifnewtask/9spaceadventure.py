welcome_screen = '''
Welcome to the Space Adventure!
Select an action (1/2):
1. Land on Mars
2. Fly to Jupiter
'''
invalid = 'Invalid Value Inserted!'
user_choice = int(input(welcome_screen))
if user_choice == 2:
    print("Your spaceship crashed. Game Over.")
elif user_choice == 1:
    user_choice = int(
        input(
        """
Now choose between (1/2):
1. Explore
2. Build a base
"""
    )
    )
    if user_choice == 1:
        print('You found alien artifacts. You Win!')
    elif user_choice == 2:
        print('You ran out of resources. Game Over.')
    else:
        print(invalid)
else:
    print(invalid)

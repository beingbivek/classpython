welcome_screen = '''
Welcome to the Underwater World!
Select an action (1/2):
1. Dive deeper
2. Surface
'''
invalid = 'Invalid Value Inserted!'
user_choice = int(input(welcome_screen))
if user_choice == 2:
    print("You returned safely.")
elif user_choice == 1:
    user_choice = int(
        input(
        """
Now choose between (1/2):
1. Search for pearls
2. Chase the fish
"""
    )
    )
    if user_choice == 1:
        print('You found a rare pearl. You Win!')
    elif user_choice == 2:
        print('You got lost underwater. Game Over.')
    else:
        print(invalid)
else:
    print(invalid)

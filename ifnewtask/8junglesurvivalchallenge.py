welcome_screen = '''
Welcome to the Jungle Survival Challenge!
Select an action (1/2):
1. Search for food
2. Build a shelter
'''
invalid = 'Invalid Value Inserted!'
user_choice = int(input(welcome_screen))
if user_choice == 2:
    print("Your shelter collapsed in the rain. Game Over.")
elif user_choice == 1:
    user_choice = int(
        input(
        """
Now choose between (1/2):
1. Hunt
2. Gather
"""
    )
    )
    if user_choice == 1:
        print('You were attacked by a wild animal. Game Over.')
    elif user_choice == 2:
        print('You found enough food. You Win!')
    else:
        print(invalid)
else:
    print(invalid)

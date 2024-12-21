welcome_screen = '''
Welcome to the Forest Adventure!
Select a path (1/2):
1. Left
2. Right
'''
invalid = 'Invalid Value Inserted!'
user_choice = int(input(welcome_screen))
if user_choice == 2:
    print("You fell into a trap. Game Over.")
elif user_choice == 1:
    user_choice = int(
        input(
        """
Now choose between (1/2):
1. Explore
2. Rest
"""
    )
    )
    if user_choice == 1:
        print('You found treasure!')
    elif user_choice == 2:
        print('You were attacked by wild animals. Game Over.')
    else:
        print(invalid)
else:
    print(invalid)
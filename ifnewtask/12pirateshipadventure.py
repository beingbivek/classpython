welcome_screen = '''
Welcome to the Pirate Ship Adventure!
Select an action (1/2):
1. Search for treasure
2. Battle enemy ships
'''
invalid = 'Invalid Value Inserted!'
user_choice = int(input(welcome_screen))
if user_choice == 1:
    user_choice = int(
        input(
        """
Now choose between (1/2):
1. Dig on the island
2. Explore the cave
"""
    )
    )
    if user_choice == 1:
        print('You found a hidden treasure chest. You Win!')
    elif user_choice == 2:
        print('You were trapped inside. Game Over.')
    else:
        print(invalid)
elif user_choice == 2:
    user_choice = int(
        input(
        """
Now choose between (1/2):
1. Attack
2. Defend
"""
    )
    )
    if user_choice == 1:
        print('You won the battle. You Win!')
    elif user_choice == 2:
        print('You were outnumbered. Game Over.')
    else:
        print(invalid)
else:
    print(invalid)

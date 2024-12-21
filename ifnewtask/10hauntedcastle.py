welcome_screen = '''
Welcome to the Haunted Castle!
Select an action (1/2):
1. Enter the castle
2. Run away
'''
invalid = 'Invalid Value Inserted!'
user_choice = int(input(welcome_screen))
if user_choice == 2:
    print("You escaped safely.")
elif user_choice == 1:
    user_choice = int(
        input(
        """
Now choose a door (1/2/3):
1. Red
2. Green
3. Black
"""
    )
    )
    if user_choice == 1:
        print('You entered a room full of flames. Game Over.')
    elif user_choice == 2:
        print('You found the treasure. You Win!')
    elif user_choice == 3:
        print('You were captured by ghosts. Game Over.')
    else:
        print(invalid)
else:
    print(invalid)

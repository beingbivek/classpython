welcome_screen = '''
Welcome to the Wizarding World!
Select a subject (1/2):
1. Spells
2. Potions
'''
invalid = 'Invalid Value Inserted!'
user_choice = int(input(welcome_screen))
if user_choice == 1:
    user_choice = int(
        input(
        """
Now choose between (1/2):
1. Practice magic
2. Compete in duels
"""
    )
    )
    if user_choice == 1:
        print('You mastered a powerful spell. You Win!')
    elif user_choice == 2:
        print('You lost to a rival wizard. Game Over.')
    else:
        print(invalid)
elif user_choice == 2:
    user_choice = int(
        input(
        """
Now choose between (1/2):
1. Brew an elixir
2. Create poison
"""
    )
    )
    if user_choice == 1:
        print('You healed a village. You Win!')
    elif user_choice == 2:
        print('Your potion backfired. Game Over.')
    else:
        print(invalid)
else:
    print(invalid)

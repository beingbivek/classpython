welcome_screen = '''
Welcome to the Cybersecurity Mission!
Select an action (1/2):
1. Trace the hacker
2. Secure the system
'''
invalid = 'Invalid Value Inserted!'
user_choice = int(input(welcome_screen))
if user_choice == 1:
    user_choice = int(
        input(
        """
Now choose between (1/2):
1. Track their IP
2. Decode their message
"""
    )
    )
    if user_choice == 1:
        print('You caught the hacker. You Win!')
    elif user_choice == 2:
        print('The message was a trap. Game Over.')
    else:
        print(invalid)
elif user_choice == 2:
    user_choice = int(
        input(
        """
Now choose between (1/2):
1. Shut down the server
2. Upgrade the firewall
"""
    )
    )
    if user_choice == 1:
        print('The attack was stopped. You Win!')
    elif user_choice == 2:
        print('The hacker bypassed it. Game Over.')
    else:
        print(invalid)
else:
    print(invalid)

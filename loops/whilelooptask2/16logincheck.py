d_username,d_password = 'admin','12345'
while True:
    i_username = input('Enter username:')
    i_password = input('Enter password:')
    if (
        d_username == i_username and
        d_password == i_password
    ):
        print("Congratulation on successfull login!")
        break
    else:
        user_input = input('Incorrect, want to try again? (y/n): ').lower()
        if user_input == 'n':
            break
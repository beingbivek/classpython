while True:
    guessed_pass = input('Guess the password: ').lower()
    if guessed_pass == 'open sesame':
        print('Access granted!')
        break
    else:
        print('Wrong Password. Try again.')

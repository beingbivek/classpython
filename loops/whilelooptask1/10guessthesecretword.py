secret_word = 'nepal'
while True:
    word = input('Guess the secret word: ').lower()
    if word == secret_word:
        print('Congratulations, you got it.')
        break
    else:
        print('Wrong guess. Try again.')
    choice = input('Do you want to continue (type \'quit\' to cancel): ').lower()
    if choice == 'quit':
        break
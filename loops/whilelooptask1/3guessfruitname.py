while True:
    fruit = input('Guess the fruit name: ').lower()
    if fruit == 'apple':
        print('Finally, you got it.')
        break
    else:
        print('Wrong guess. Try again.')

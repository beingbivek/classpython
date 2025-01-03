while True:
    user_num = int(input('Enter a number: '))
    if user_num % 2 == 0:
        print(user_num,'is even.')
    else:
        print(user_num,'is odd.')
    user_choice = input('Want to continue? (y/n): ').lower()
    if user_choice == 'n':
        break
gl = 'good luck'
count = 0
while count < 3:
    name = input('Enter phrases: ')
    if name == gl:
        if count == 3:
            print('You typed goodluck three times.')
            break
        count += 1
        print(f'You typed the same word {count} times.')
    
from random import randint
attempt = 1
randnum = randint(1,10)
while True:
    guessednum = int(input("Enter your guess number (1 to 10): "))
    if guessednum < randnum:
        attempt += 1
        print('Guess Higher!')
    elif guessednum > randnum:
        attempt += 1
        print('Guess Lower!')
    else:
        print(f"You guessed it correctly in {attempt}th attempts!")
        break
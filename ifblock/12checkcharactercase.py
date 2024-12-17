character = input("Enter a character: ")
if character.isdigit():
    print(f'{character} is a Digit.')
else:
    if character.isupper():
        print(f'{character} is in Upper Case.')
    else:
        print(f'{character} is in Lower Case.')
user_string = input('Enter a long string: ')  
digit_counter = letter_counter = space_counter = 0 
i = 0
while i < len(user_string):
    if user_string[i].isdigit():
        digit_counter += 1
    elif user_string[i].isalpha():
        letter_counter += 1
    elif user_string[i].isspace():
        space_counter += 1
    i += 1
print(
    'The number of digits are: ',digit_counter,
    'The number of letters are: ',letter_counter,
    'The number of spaces are: ',space_counter,sep = '\n'
)
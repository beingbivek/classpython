user_input = input("Enter a long sentences with numbers: ")
number_of_space = number_of_digits = number_of_letters = 0
for i in user_input:
    if str(i).isspace():
        number_of_space += 1
    elif str(i).isdigit():
        number_of_digits += 1
    elif isinstance(i,str):
        number_of_letters += 1
else:
    print(
        "The number of digits: ",number_of_digits,
        "The number of letters: ",number_of_letters,
        "The number of spaces: ",number_of_space
    )
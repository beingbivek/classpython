user_input = input("Enter long string with a lot of spaces: ")
no_of_spaces = 0
for i in user_input:
    if str(i).isspace():
        no_of_spaces += 1
print("Total no of spaces are: ",no_of_spaces)
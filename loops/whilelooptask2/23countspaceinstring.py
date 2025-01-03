user_input = input('Enter long strings with spaces: ')
counter_space = i = 0
while i < len(user_input):
    if user_input[i].isspace():
        counter_space += 1
    i += 1
print('The number of spaces is: ',counter_space)
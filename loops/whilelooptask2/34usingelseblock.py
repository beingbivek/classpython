isPlaying = True
while isPlaying:
    a = int(input('Enter a number: '))
    b = int(input('Enter a number: '))
    sum = a + b
    print("The sum is: ",sum)
    user_choice = input('Do you want to continue (y/n): ').lower()
    if user_choice == 'n':
        isPlaying = False
else:
    print('Thanks for playing!')
while True:
    num = int(input("Enter a number: "))
    prime,i = 0,1
    while i <= num:
        if num % i == 0:
            prime += 1
        i += 1
    if prime == 2:
        print('The number is prime!')
    else:
        print('The number is not prime!')
    choice = input('Do you want to continue (y/n): ').lower()
    if choice == 'n':
        break
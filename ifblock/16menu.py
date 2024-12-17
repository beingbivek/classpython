menuitems = {'pizza': 10, 'burger': 7, 'pasta': 8}
print("Choose an option to know the price: ")

i = 1
for menu in menuitems:
    print(f'{i} {menu}')
    i+=1

userchoice = int(input())

if userchoice == 1:
    print(f'The price of pizza is {menuitems["pizza"]}')
elif userchoice == 2:
    print(f'The price of burger is {menuitems["burger"]}')
elif userchoice == 3:
    print(f'The price of pasta is {menuitems["pasta"]}')
else:
    print("Invalid choice")
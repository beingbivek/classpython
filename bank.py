balance = 5000
menuoptions = '''Welcome to the ATM!
1. Balance Inquiry
2. Withdraw Cash
3. Deposit Cash
4. Exit'''
print(menuoptions)

choice = int(input("Please enter your choice (1-4): "))

if choice == 1:
    print(f"Your current balance is: {balance}")

elif choice == 2:
    amount = int(input("Enter the amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient Amount!")
    elif amount <= balance:
        balance -= amount
        print(f"Rs. {amount} have been deducted, now your balance is Rs.{balance}")
    else:
        print(f"Invalid Amount!")

elif choice == 3:
    amount = int(input("Enter the amount to be deposit: "))
    if amount <= 0:
        print("Invalid Amount!")
    else:
        balance += amount
        print(f'Deposite successfully, Your new balance is Rs.{balance}')

elif choice == 4:
    print("Thank you for using ATM. Goodbye!")

else:
    print("Invalid choice. Please try again.")
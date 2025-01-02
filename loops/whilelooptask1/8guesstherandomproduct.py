import random
isExit = False
while (not isExit):
    a = random.randint(1,30)
    b = random.randint(1,30)
    product = a * b
    user_input = int(input("Enter your guess number: "))
    if user_input == product:
        print(f"Correct!, The product of {a} and {b} is: ",product)
    else:
        print(f"Incorrect, the answer was {product}, try again!")
    user_decision = input("Do you want to continue (y/n): ").lower()
    if user_decision == 'n':
        print("Thanks for playing")
        isExit = True
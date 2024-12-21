vegornonveg = '''
Welcome to our Restro!
Choose (1/2)
1. Veg
2. Non-Veg
'''
vegoption = '''
Vegeterian Menu
Choose (1/2)
1. Salad
2. Pasta
'''
nonvegoption = '''
Non-Vegiterian Menu
Choose (1/2)
1. Chicken
2. Fish
'''
wrong_order = "Wrong Order!"
user_choice = int(input(vegornonveg))

if user_choice == 1:
    user_choice = int(input(vegoption))
    if user_choice == 1:
        print("Your Salad will be served soon!")
    elif user_choice == 2:
        print("Your Pasta will be served soon!")
    else:
        print(wrong_order)
elif user_choice == 2:
    user_choice = int(input(nonvegoption))
    if user_choice == 1:
        print("Your Chicken will be served soon!")
    elif user_choice == 2:
        print("Your Fish will be served soon!")
    else:
        print(wrong_order)
else:
    print(wrong_order)
while True:
    age = int(input("Enter your age: "))
    if age < 18:
        print("You are a minor.")
    elif 18 <= age <= 60:
        print("You are an adult.")
    elif age > 60:
        print("Your are a senior citizen.")
    else:
        print('Invalid Age')
    user_choice = input("Do you want to stop then type stop: ").lower()
    if user_choice == 'stop':
        break
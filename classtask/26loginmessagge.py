username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "passcode":
        print("Welcome, Access Granted!")
    else:
        print("Incorrect password!")
else:
    print("Incorrect username!")

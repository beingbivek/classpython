print("Welcome to Mobile Banking")
uname = input('Enter a username: ')
password = input("Enter a password: ")

for i in range(3,0,-1):
    username = input("Enter your username: ")
    passkey = input("Enter your password: ")
    if (
        uname != username
        or passkey != password
        or username == ''
        or passkey == ''
    ):
        if i == 1:
            continue
        print(f"Wrong Username or Password, {i-1} attempts left.")
    else:
        print("Successful Login")
        break
else:
    print("You are blocked")